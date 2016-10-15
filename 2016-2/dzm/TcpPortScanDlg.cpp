// TcpPortScanDlg.cpp : 实现文件

#include "stdafx.h"
#include "TcpPortScan.h"
#include "TcpPortScanDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

//对话框类
class CAboutDlg : public CDialog //CAboutDlg这个类以public的方式继承于CDialog
{
public:
	CAboutDlg();

//会话数据
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };  //enum为枚举类型
	//}}AFX_DATA

	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    //DDX将数据成员变量和对话类模板内的控件连接，使得数据在控件之间很容易地传输。
	//}}AFX_VIRTUAL

// Implementation
protected:
	//{{AFX_MSG(CAboutDlg)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
	//{{AFX_DATA_INIT(CAboutDlg)
	//}}AFX_DATA_INIT
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAboutDlg)
	//}}AFX_DATA_MAP
}

//宏定义的一种
BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
	//{{AFX_MSG_MAP(CAboutDlg)
		// No message handlers
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CTcpPortScanDlg dialog

CTcpPortScanDlg::CTcpPortScanDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CTcpPortScanDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CTcpPortScanDlg)
	m_Address = _T("");
	m_Port = _T("");
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CTcpPortScanDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CTcpPortScanDlg)
	DDX_Control(pDX, IDC_LIST1, m_list);
	DDX_Text(pDX, IDC_EDIT_ADDRESS, m_Address);
	DDX_Text(pDX, IDC_EDIT_PORT, m_Port);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CTcpPortScanDlg, CDialog)
	//{{AFX_MSG_MAP(CTcpPortScanDlg)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON1, OnTcpscan)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CTcpPortScanDlg message handlers

BOOL CTcpPortScanDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	
	// TODO: Add extra initialization here
	LONG lStyle;
	lStyle = GetWindowLong(m_list.m_hWnd, GWL_STYLE);//获取当前窗口style
	lStyle &= ~LVS_TYPEMASK; //清除显示方式位
	lStyle |= LVS_REPORT; //设置style
	SetWindowLong(m_list.m_hWnd, GWL_STYLE, lStyle);//设置style
	DWORD dwStyle = m_list.GetExtendedStyle();
	dwStyle |= LVS_EX_FULLROWSELECT;//选中某行使整行高亮（只适用与report风格的listctrl）
	dwStyle |= LVS_EX_GRIDLINES;//网格线（只适用与report风格的listctrl）
	m_list.SetExtendedStyle(dwStyle); //设置扩展风格
	CRect rc;
	m_list.GetClientRect(rc);
	int width=rc.Width()/3;
	m_list.InsertColumn(0,"主机地址",LVCFMT_CENTER,width);
	m_list.InsertColumn(1,"端口号",LVCFMT_CENTER,width);
	m_list.InsertColumn(2,"端口状态",LVCFMT_CENTER,width);
	
	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CTcpPortScanDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CTcpPortScanDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CTcpPortScanDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CTcpPortScanDlg::OnTcpscan() 
{
	UpdateData(true);                         //MFC窗口函数，用来刷新数据
	int count=m_list.GetItemCount();          
	WSADATA WSAData;                          //用来存储被WSAStartup函数调用后返回的Windows Sockets数据
	if(WSAStartup(MAKEWORD(2,2),&WSAData)!=0) /*这个函数是连接应用程序与winsock.dll的第一个调用.其中,第一个参数是WINSOCK 版本号,第二个参数是指向
                                              WSADATA的指针.该函数返回一个INT型值,通过检查这个值来确定初始化是否成功*/
	{
		MessageBox("初始化Winsock失败!");
		return;
	}
	Socket=socket(AF_INET,SOCK_STREAM,0);         //创建连接套接字
	if(Socket==INVALID_SOCKET)
	{
		MessageBox("创建Socket失败!");
		WSACleanup();                         //该函数用于终止Winsock.DLL的使用
		return;
	}
	int IpAddress;								  //判断域名或IP地址
	IpAddress=inet_addr(m_Address);
	if(IpAddress==INADDR_NONE)
	{
		hostent* pHostent=gethostbyname(m_Address);
		if(pHostent)
			IpAddress=(*(in_addr*)pHostent->h_addr).s_addr;
	}	
	sockaddr_in DestHost;                         //定义套接字地址
	memset(&DestHost,0,sizeof(DestHost));
	DestHost.sin_family=AF_INET;
	DestHost.sin_port=htons(atoi(m_Port));
	DestHost.sin_addr.s_addr=IpAddress;
	int nConnect;                                 //与服务器建立连接
	nConnect=connect(Socket,(sockaddr*)&DestHost,sizeof(DestHost));  //调用connect()
	if(nConnect==SOCKET_ERROR)
	{
		m_list.InsertItem(count,m_Address);
		m_list.SetItemText(count,1,m_Port);
		m_list.SetItemText(count,2,"close");
	}
	else
	{
		m_list.InsertItem(count,m_Address);
		m_list.SetItemText(count,1,m_Port);
		m_list.SetItemText(count,2,"open");
	}
	UpdateData(false);
	closesocket(Socket);
	WSACleanup();                                 //释放套接字绑定
}

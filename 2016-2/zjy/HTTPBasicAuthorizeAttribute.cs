//这个代码，实现了HTTP基本认证的类。读了这篇代码后，我分析了一下代码结构，根据自己的理解做了一些注释。
//虽然仅仅这些代码远远不能实现Basic认证过程，但可以帮助我更好的理解，所以先存下来。
//例：当用户名为Parry，密码为123456时，HTTP Basic认证实现过程。

using System;
using System.Text;

namespace WebAPI.UserCenter
{
    //基于System.Web.Http.AuthorizeAttribute类实现HTTPBasic认证的类
    public class HTTPBasicAuthorizeAttribute : System.Web.Http.AuthorizeAttribute
    {
        //实现方法：OnAuthorization 认证过程
        public override void OnAuthorization(System.Web.Http.Controllers.HttpActionContext actionContext)
        {
            if (actionContext.Request.Headers.Authorization != null)
            {
                //Base64 ing(●'◡'●)
                string userInfo = Encoding.Default.GetString(Convert.FromBase64String(actionContext.Request.Headers.Authorization.Parameter));

                //Compare以验证是否一致
                if (string.Equals(userInfo, string.Format("{0}:{1}", "Parry", "123456")))
                {
                    IsAuthorized(actionContext);
                }
                else
                {
                    HandleUnauthorizedRequest(actionContext);
                }
            }
            else
            {
                HandleUnauthorizedRequest(actionContext);
            }
        }
       
        //实现方法：HandleUnauthorizedRequest,以实现验证失败时继续提示验证
        protected override void HandleUnauthorizedRequest(System.Web.Http.Controllers.HttpActionContext actionContext)
        {
            var challengeMessage = new System.Net.Http.HttpResponseMessage(System.Net.HttpStatusCode.Unauthorized);
            challengeMessage.Headers.Add("WWW-Authenticate", "Basic");
            throw new System.Web.Http.HttpResponseException(challengeMessage);
        }
    }
}



//完成此类后，在需要启用HTTP基本认证的Controller的类加上属性[HTTPBasicAutherize]
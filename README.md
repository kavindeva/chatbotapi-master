# IIS Deployment Configurations
This setup process shows how to deploy a Python project on Internet Information Service(IIS) with the help of FastCGI 
Framework which is used to deploy any python application without any hustle.

This demonstration setup will applicable to deploy all other python applications such as [chatbotapi.py](https://github.com/kavindevarajan/chatbotapi/blob/master/chatbotapi.py) in chatbotapi 
repository, [file_upload.py](https://github.com/kavindevarajan/file_upload/blob/master/file_upload.py) in file_upload repository, [app.py](https://github.com/kavindevarajan/teams-iassist/blob/master/app.py) in MSteams integration repository.

### Step 1:
- Run CMD prompt as admin and executed IISRESET command to reset IIS
- ![iis-demo-1](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-1.png)

### Step 2:
- Verify all required python packages whether it is present are not.
- ![iis-demo-2](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-2.png)

### Step 3:
- Install FastCGI python library
- [FastCGI <fastCgi>](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/fastcgi/) - Installation documentation
```bash
pip install wfastcgi
```

### Step 4:
- Ran IIS server as admin and fastCGI is installed.
- ![iis-demo-3](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-3.png)

### Step 5:
- To setup a path in fastCGI settings execute the below command wfastcgi-enable.exe in this path C:\Python\Scripts
- ![iis-demo-4](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-4.png)

### Step 6:
- Verified in  IIS server fastCGI settings whether it is present or not.
- ![iis-demo-5](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-5.png)

### Step 7:
- Created a repository called chatbotapi under C:\inetpub\wwwroot, create a flask application called "chatbotapi.py", 
- a web.config file shown below and then copied the wfastcgi.py file from C:\Python\Lib\site-packages then pasted it in
- under C:\inetpub\wwwroot\chatbotapi. Picture shown below.
- **[chatbotapi.py](https://github.com/kavindevarajan/chatbotapi/blob/master/chatbotapi.py)**
- **web.config**
```
<?xml version="1.0" encoding="UTF-8"?>
 <configuration>
   <system.webServer>
       <handlers>
           <add name="iassist-Chatbot" path="*" verb="*" modules="FastCgiModule" scriptProcessor="C:\Python\python.exe|C:\inetpub\wwwroot\chatbotapi\wfastcgi.py" resourceType="Unspecified" requireAccess="Script" />
       </handlers>
   </system.webServer>
 </configuration>
```

### Step 8:
- Chatbotapi directory should looks like this.
- ![iis-demo-6](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-6.png)

### Step 9:
- Now, we have to provide a few permissions to IIS so that it can access the chatbotapi directory. Open a CMD and change the directory to chatbotapi and execute the following commands:
From <https://medium.com/@dpralay07/deploy-a-python-flask-application-in-iis-server-and-run-on-machine-ip-address-ddb81df8edf3> 

Executed below both commands and 0 unsuccessful

- ![iis-demo-7](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-7.png)

### Step 10:
- Created a chatbotapi application under iAssist.laninnovations.com web site pool:  (Assigned Port number 80)
- ![iis-demo-8](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-8.png)
- After creating website application pool and applications it should look like this.
- ![iis-demo-9](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-9.png)

### Step 11:
- Now setup Handler mapping in handler mapping settings under /bot:
- ![iis-demo-10](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-10.png)

### Step 12:
- Click request Restrictions ----> Make sure this checkbox is unticked or not.
- ![iis-demo-11](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-11.png)

### Step 13:
- After creating module in handler mapping verify whether this new wfastcgi.py file path is present in fastcgi 
settings or not.
- ![iis-demo-12](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-12.png)

### Step 14:
- Double click the application entry in FastCGI settings to edit the application and select “Environment Variables”.
- ![iis-demo-13](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-13.png)

### Step 15:
- IIS have to access iAssist_IT_support folder to access datasets, model file, model results, new datasets and User data
- ![iis-demo-14](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-14.png)
- ![iis-demo-15](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-15.png)

### Step 16:
- IIS have to access iAssist_IT_support folder to access datasets, model file, model results, new datasets and User data
- ![iis-demo-16](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-16.png)
- ![iis-demo-17](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-17.png)

### Step 17:
- Finally check whether this application is working or not. Or else debug again.
- ![iis-demo-18](https://github.com/kavindevarajan/chatbotapi/blob/master/IIS-demo-images/iis-demo-18.png)

##  ����bro�ļ��������ȡ֤ʵս����

### д��ǰ��
- ʲô�Ǽ��������ȡ֤
```
�����ȡ֤�����ü����������ؿ�ѧ�ͼ�����ԭ��ͷ�����ȡ��������ص�֤����֤��ĳ���͹���ʵ�Ĺ��̡������������֤�ݵ�ȷ�����ռ����������������鵵�Լ���ͥ��ʾ��
```

- bro���
```
Bro��һ��Vern Paxsonʵ�ֵ�ʵʱ�������ּ���������98����ⷢ����BSD license������������Ŀ����ʵ��һ����100M������ʵʱ�澯����������Է��롢�߿���չ�Ե����ּ�⼰����������ϵͳ��
Bro��һ����Ŀ�Դ����������������Ҫ���ڶ���·���������εĿ�����Ϊ��������һ����ȫ��ء���ͨ�׵�˵���ǣ�Bro֧���ڰ�ȫ��֮����д�Χ�����������������������������ʹ���λ��
```
broaϵͳ�ṹ����ͼ��ʾ��

![](image/bro.PNG)

###  ʵ��Ҫ��
ʹ��bro��Դ����������ͨ�������������е�extract file��log�ļ��õ�����������IP

###  ʵ�����

##### ��������

- ��װbro
  - apt install bro bro-aux
- �༭bro�����ļ�
  - �༭ `/etc/bro/site/local.bro`,���ļ�β���������������ô���
  ![](image/��������.PNG)

  - ˵����
  ```
  @load ����module�ж���������ռ�
  @load frameworks/files/extract-all-files ��ʾ��ȡ�����ļ�
  @load mytuning.bro ��ʾ����mytuning.bro�������Լ���д��ָ��
  ```

  - ��`/etc/bro/site/`Ŀ¼�´������ļ�mytuning.bro,����Ϊ
  ```
  redef ignore_checksums=T;##����У�����֤
  ```
  ![](image/�½��ļ�.PNG)

##### ��������

- ����pcap����ʵ��Ŀ�꣩
![](image/����pcap��.PNG)
```
wget  https://www.honeynet.org/files/attack-trace.pcap_.gz
```

- ��ѹ����ʹ��bro�Զ�����pcap��
```
bro -r attack-trace.pcap_ /etc/bro/site/local.bro
```

  >�������¾�����Ϣ�����ڱ�������ȡ֤ʵ����˵û��Ӱ��
```
WARNING: No Site::local_nets have been defined. It's usually a good idea to define your local networks.
```

- �鿴attack-trace.pcap�ļ��ĵ�ǰĿ¼
  - ��һЩ.log�ļ���һ��extract_files�ļ���
  ![](image/ls.PNG)
  - ��extract_files�ļ����з���һ���ļ�

  ![](image/extract_files���ļ�.PNG)

  �����ļ��ϴ���[ThreatBook](https://x.threatbook.cn)����ƥ����һ����ʷɨ�豨��,�ñ����������һ����֪�ĺ��ų���
  ![](image/����.PNG)


- �Ķ�/usr/share/bro/base/files/extract/main.bro��Դ�����е�on_odd�������˽⵽���ļ���������һ��"-"�������ַ����� `files.log` �е��ļ�Ψһ��ʶ
![](image/on_odd.PNG)

- �鿴`files.log`�ɵ�
  - ���ļ���ȡ��FTP�Ự
  - �ļ���Ψһ��ʶ����`FHUsSu3rWdP07eRE4l`
  - ��������`conn_uids`Ϊ`Cmy8VGL5YkUfwKhfj`

  ![](image/files.PNG)

- �鿴`conn.log`
  - �ҵ�idΪ`Cmy8VGL5YkUfwKhfj`����Ԫ����Ϣ���õ���PE�ļ�������IPv4��ַΪ98.114.205.102������
  ![](image/conn.PNG)
  
  - Ҳ����ʹ��`bro-cut ts uid id.orig_h id.resp_h proto < conn.log`���鿴
  ![](image/log�ļ���ʾ��С����.PNG)

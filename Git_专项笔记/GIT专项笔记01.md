# GIT�ֲ�

[TOC]

## ��һ�� GIT��װ

```shell
sudo apt-get install git
```

������Դ���� ���밲װ

GITʹ�ó�ʼ��


```shell
#ע��GIT
git config --global user.name  "�û���"
git config --global user.email "����"
```


```shell
#�鿴������ 
git config --list
```



```txt
GIT������
	1-�ڹ���Ŀ¼������޸��ļ�
	2-����Ҫ���а汾������ļ���������ݴ���
	3-���ݴ������ļ�����GIT�ֿ�

GIT������ļ�������״̬
	���޸� 	modified
	���ݴ�		staged
	���ύ		committed
```



```shell
#�����ֿ� 
git init
#�ļ��²��� .git�ļ�

#����ļ� 
git add readme_file.md

git add * 	#��ӹ���Ŀ¼��������ļ�
git add .	#Ч��ͬ��

#�ύ�ݴ����ļ����ֿ�

git commit -m "add a readme file"
```


```shell
#������Ŀ¼���ļ�����ŵ�GIT�ֿ���Ҫ����
git add �ļ���
git commit -m "�����ɶ"
```



## �ڶ���

```shell
#�鿴GIT״̬ 
git status
#����LICENSE  ��MITЭ��д��
#ͬ�ļ�����������û�з���git����ļ� ����git status ʱ��ʾ
```



```shell
#���ط����� 
#�ͷ�ָ���ݴ����ڵ��ļ�
git reset HEAD filename.txt
	
#�ͷ����һ�ν����ݴ������ļ�
git reset HEAD 

#�����ļ��� 
#���ݴ�����LICENSE�ļ����ǵ��������Ĺ���LICENSE�ļ�
git checkout -- LICENSE  
	
#������LICENSE�ļ����޸ĺ�  ʹ��git status�鿴  
#������ݴ����͹���������LICENSE�ļ�
```


```shell
#�鿴��ʷ�ύ��¼ 
git log
```

## ������

```shell
#reset �� checkout

#�ڲֿ���� ָ��������һ������ ���ݴ����ָ�Ϊ�ÿ���
git reset HEAD~	
	
#����һ������
git reset HEAD~~ 
	
#ǰN������   ���˺Ÿ���
git reset HEAD~N 

```



```shell
#reset�����ѡ��
git reset --mixed HEAD~   	#��Ĭ��ָ�
	
#�ƶ�HEAD��ָ�� ����һ������
#��HEAD�ƶ���ָ��Ŀ��ջع����ݴ���

git reset --soft HEAD~ 

#�ƶ�HEAD��ָ�� ����һ������  �൱�ڳ�����һ���ύ

git reset --hard HEAD~

#�ƶ�HEAD��ָ�� ����һ������  �൱�ڳ�����һ���ύ
#��HEAD�ƶ���ָ��Ŀ��ջع����ݴ�����
#���ݴ������ļ���ԭ������Ŀ¼
--soft 	#�ƶ�HEAD��ָ��
--mixed	#�����ջع����ݴ���
--hard	#���ݴ�����ԭ������Ŀ¼
```


```shell
#�ع�ָ������  �ع������ļ�
#ָ������ID	
git reset  �ļ�SHA1��ϣֵ���汾����ID�ţ�
```

?	

## ���Ŀ�

```shell
#���������ļ��� MyProject2 

#������Ŀ����	
git init  

#����README.md�ļ�
touch README.md

#�ύ���ݴ���	
git add �ļ� 	

#�ύ��Ŀ	
git commit -m "ע��"
```

  	

```shell
#�޸Ĺ������ڵ��ļ�����
#�ȽϹ������ļ����ݴ����ļ�	
git diff 

	index ���ļ�ID  ���ļ�ID    ���ļ�Ȩ�����ļ�Ȩ��
	---	Ϊ�ݴ������ļ�
	+++	Ϊ���������ļ�

	��+��Ϊ���ļ����е�

	J K ���¼�  
	F���·�ҳ   D���·���ҳ U ���Ϸ���ҳ

	g ��ת�����һ��  
	G ��ת����һ��

	3  g   ��ת��������

	/ ������������
	��������������
	n ��һ��ƥ����

	h ��������ĵ�
	q �˳�

#�Ƚϲֿ��в�ͬ����ʷ����
git diff ����1��ID  ����2��ID
```


```shell
#�ȽϹ������кͲֿ��еĿ���
git diff ����ID    	
git diff HEAD
```

```shell
#�Ƚ��ݴ����кͲֿ��еĿ���
git diff --cached 	  	#���Ƚϲֿ����¿��գ�
git diff --cached  ID	#���Ƚϲֿ�ָ�����գ�
```

?	

## �����

```shell
#���������
#1 �汾���ύ���ֿ⣬����©�������ļ�û�����
#2 �汾�ύ���ְ汾˵��д�Ĳ���ȫ�� �޷���ʾ�޸�����

#�޸����һ���ύ 
#ִ�д� --amend ѡ��� commit �ύ����
#GIT�ͻ�������һ���ύ
git commit --amend  --m "˵��"

#�����½����޸��ύ˵��
#���� i ��  ��ʼ���     backspaceɾ���ı�
#ESC�Ƴ��༭ģʽ   
#shift������Z  �����Ƴ�
#:q! �������˳�

#�������е��ļ��ָ���������
git checkout -- README.md

#ɾ�����������ݴ���ĳ���ļ� ��ȡ������ �´��ύ������ֿ⣩ 
git rm �ļ���		

#��ָ��ָ����ϸ����� ������һ���ύ
git checkout HEAD~

#ǿ��ɾ�� �ݴ��� �� ����Ŀ¼���ļ�
git rm -f �ļ���

#����ɾ���ݴ����ļ�  �����������ļ�
git rm --cached �ļ���

#�������ļ�
git mv ���� ����

#������� 
ren/mv 	���� ����
git rm 	����
git add ����
```

## ������


	#������֧
	git branch ��֧����


```shell
#�鿴һ�� 
git log --decorate --oneline 
	--decorate #��ʾ����ָ����յ�����
	--oneline #�����ʾ	
	--graph #ͼ����ʾ
	--all #��ʾ���з�֧

git log --decorate --oneline --graph --all

#�л���֧
git checkout ��֧����
```

## ���߿�


```shell
#ʵ�ʿ�����֧ 
#	master		������֧
#	hotfix		BUG�޸���֧
#	release		���ܼ��ϱ���
#	develop		�������Է�֧
#	feature		���ܿ�����

#�ϲ���֧
git merge ��֧����

#��������֧����ͬ���Ҷ��޸Ĺ����ļ�  ���� ��ͻ

#�޸��ļ��� 
git mv ���� ����	

#��������ԭ����֧
git checkout -b ��֧����

#ɾ����֧ 
git branch -d ��֧����
```


?	Զ��
```shell
#�޸�Զ�ֿ̲�ı��ر���
git remote rename oldname newname 
#�Ƴ���Զ�ֿ̲������
git remote rm old_reposity_name 
#�����ֿ�   originΪĬ�� ���Ը�Ϊ��������
git remote add origin git_remote_address
git remote add github git@github.com:User/RepoName.git
git remote add gitee git@gitee.com:User/RepoName.git
 
```

Զ������


```shell
#���͵� origin �������ӵ�Զ�ֿ̲� �� �� master ��֧  
# -u ����   �ѱ��ص�master��֧�������͵�Զ���µ�master��֧������ѱ��ص�master��֧��Զ�̵�master��֧�������� ���Լ�����
git push -u origin master
```

 

## �ڰ˿�

```sh
#������֧ 
#����ʵ��

#reset Ĭ��ֻ��ָ�����ļ��ָ����ݴ��� 
#reset �޷���ʹ���� --soft �� --hard ����ָ���ļ�

#checkout ͬʱ�����ݴ����͹�����

#reset ������ƶ�HEADָ�루--soft�� 
#-> �����ݴ�����--mixed��Ĭ�ϣ�
#-> ���ǹ�������--hard��

#checkout �л�ָ�� Ȼ�� �����ݴ����͹�����

#�����reset --hard ��˵ checkout ������Ӱ�ȫ��
#checkout���л���֮ǰ���鵱ǰ����״̬
#������ǡ�clean���Ļ� GIT��������ִ�в��� 
#��  reset --hard �򸲸���������
```




















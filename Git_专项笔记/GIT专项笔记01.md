# GIT�ֲ�

[TOC]

## ��һ�� GIT��װ

```shell
sudo apt-get install git
```

������Դ���� ���밲װ

### GITʹ�ó�ʼ��


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

### �������

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

#���Զ�ֿ̲�
git remote add origin https://git_remote_address.git

#����Զ�ֿ̲�
git push origin
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

# �鿴��ǰ�ݴ����ļ�
git ls-files
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

#����ĳ���ļ����ݴ����ڵĸ���
git checkout �ļ���
git restore �ļ���

#������ǰĿ¼�����е����ݴ����ڵĸ���
git checkout .
git restore .

#��ָ��ָ����ϸ����� ������һ���ύ
git checkout HEAD~

#ǿ��ɾ�� �ݴ��� �� ����Ŀ¼���ļ�
git rm -f �ļ���

#����ɾ���ݴ����ļ�  �����������ļ�
git rm --cached �ļ���

#��ʾδ���ٵ��ļ�
git clean -dn
#ɾ������δ�����ļ�
git clean -df

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
git switch -c ��֧����

#ɾ����֧ 
git branch -d ��֧����
```


Զ��
```shell
#�鿴Զ�ֿ̲�
git remote -v
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



## �ھſ� �����ͻ�ԭ

����δ���ٵı��

```shell
######����δ���ٵı��  ����δ�����ļ��ı��#####

#����ĳ��δ�����ļ��ĸ���
git checkout �ļ���
git restore �ļ���
Updated 1 paths from the index

#������ǰĿ¼������δ�����ļ��ĸ���
git checkout .
git restore .
Updated 2 paths from the index

#��ʾδ���ٵ��ļ�
git clean -dn
#ɾ������δ�����ļ�
git clean -df

```

�����Ѹ��ٵı�� 

```shell
######�����Ѹ��ٵĵı��  ���������ݴ����ļ��ı��#####

#�ļ��������
git add test.txt
warning: LF will be replaced by CRLF in second.txt.
The file will have its original line endings in your working directory

#��ͼ��ԭ�ļ� ��û�гɹ�
git checkout test.txt
Updated 0 paths from the index

#�鿴״̬
git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   test.txt
#���ݲ���
git reset  test.txt
git restore --staged test.txt
Unstaged changes after reset:
M       test.txt

#��ԭ�ļ��ɹ�
git checkout test.txt
Updated 1 paths from the index
 
```

### �ύ����

```shell
#�����ļ�
echo 'test' > test.txt

#�����ļ�
git add test.txt
warning: LF will be replaced by CRLF in unrequired.txt.
The file will have its original line endings in your working directory

#�鿴�����ļ�
git ls-files
.gitignore
test.txt

#�ύ
git commit -m 'test file added'
[master db9cca2] test file added
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

#�鿴��־
git log
commit db9cca2fd80f8489cd9d6000a74f4e6dee7beecd (HEAD -> master)
Author: sky92archangel <sky92@DESKTOP-P8SB3R8>
Date:   Sat Mar 18 16:20:41 2023 +0800

    test file added

commit a19c8053b448e48b4ea2638ec58d3677d6e3b3bd
Author: sky92archangel <sky92@DESKTOP-P8SB3R8>
Date:   Sat Mar 18 16:09:57 2023 +0800

    my-first-commit

#����һ�� ������ ɾ�����һ���ύ �������е��ļ�����Ƴ��ݴ���
git reset --soft HEAD~1
#����һ�� Ӳ���� ɾ�����һ���ύ ��Ӳ���ļ�ʵʱ��� 
git reset --hard HEAD~1

#�ٴβ鿴��־
git log
commit a19c8053b448e48b4ea2638ec58d3677d6e3b3bd (HEAD -> master)
Author: sky92archangel <sky92@DESKTOP-P8SB3R8>
Date:   Sat Mar 18 16:09:57 2023 +0800

    my-first-commit
 
 
```

### ɾ����֧

```shell
#ɾ�������֧
git branch -D second-branch third-branch
git branch -d second-branch third-branch
 
```

### ��ʱ��Ⱥ��֧

```shell
#�鿴��־
git log
commit db9cca2fd80f8489cd9d6000a74f4e6dee7beecd (HEAD -> master)
Author: sky92archangel <sky92@DESKTOP-P8SB3R8>
Date:   Sat Mar 18 16:20:41 2023 +0800

    test file added

commit ed8a19a0b240541e79600659ed25e5b7830c1441
Author: sky92archangel <sky92@DESKTOP-P8SB3R8>
Date:   Sat Mar 18 16:09:57 2023 +0800

    my-first-commit
    
#��ĳ���ύ״̬������Ⱥ��֧
git checkout ed8a19a0b240541e79600659ed25e5b7830c1441 

Note: switching to 'ed8a19a0b240541e79600659ed25e5b7830c1441'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at ed8a19a reset test
 
#�޸��ļ� ���ύ
echo 'gogog' > unrequired.txt && git add . && git commit -m 'change test file'

warning: LF will be replaced by CRLF in unrequired.txt.
The file will have its original line endings in your working directory
[detached HEAD 2f880cd] change test file
 1 file changed, 1 insertion(+), 1 deletion(-)

#�ص�һ���֧
git switch master
Warning: you are leaving 1 commit behind, not connected to
any of your branches:

  2f880cd change test file

If you want to keep it by creating a new branch, this may be a good time
to do so with:

 git branch <new-branch-name> 2f880cd

Switched to branch 'master'
  
#������Ⱥ��֧
git branch detached-head 2f880cd    
#ת����֧
git switch detached-head
Switched to branch 'detached-head'

#�鿴�÷�֧
git log
commit 2f880cd85ab35ff4c66c01e8dc843722980d0a2b (HEAD -> detached-head)
Author: sky92archangel <sky92@DESKTOP-P8SB3R8>
Date:   Sat Mar 18 16:48:37 2023 +0800

    change test file

#�ص�һ���֧
git switch master
Switched to branch 'master'

#�ϲ�
git merge detached-head
 
  
    
    
    
    
    

```








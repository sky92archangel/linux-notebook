# GIT手册

[TOC]

## 第一课 GIT安装

```shell
sudo apt-get install git
```

或下载源代码 编译安装

GIT使用初始化


```shell
#注册GIT
git config --global user.name  "用户名"
git config --global user.email "邮箱"
```


```shell
#查看看配置 
git config --list
```



```txt
GIT工作流
	1-在工作目录中添加修改文件
	2-将需要进行版本管理的文件爱你放入暂存区
	3-将暂存区的文件交道GIT仓库

GIT管理的文件有三种状态
	已修改 	modified
	已暂存		staged
	已提交		committed
```



```shell
#建立仓库 
git init
#文件下产生 .git文件

#添加文件 
git add readme_file.md

git add * 	#添加工作目录里的所有文件
git add .	#效果同上

#提交暂存区文件到仓库

git commit -m "add a readme file"
```


```shell
#将工作目录的文件爱你放到GIT仓库需要两步
git add 文件名
git commit -m "你干了啥"
```



## 第二课

```shell
#查看GIT状态 
git status
#创建LICENSE  将MIT协议写入
#同文件夹下新增且没有放入git里的文件 会在git status 时提示
```



```shell
#返回方法： 
#释放指定暂存区内的文件
git reset HEAD filename.txt
	
#释放最后一次进入暂存区的文件
git reset HEAD 

#覆盖文件： 
#把暂存区的LICENSE文件覆盖到工作区改过的LICENSE文件
git checkout -- LICENSE  
	
#工作区LICENSE文件被修改后  使用git status查看  
#会出现暂存区和工作区两个LICENSE文件
```


```shell
#查看历史提交记录 
git log
```

## 第三课

```shell
#reset 和 checkout

#在仓库汇中 指向代码的上一个快照 将暂存区恢复为该快照
git reset HEAD~	
	
#再上一个快照
git reset HEAD~~ 
	
#前N个快照   波浪号个数
git reset HEAD~N 

```



```shell
#reset命令的选项
git reset --mixed HEAD~   	#（默认指令）
	
#移动HEAD的指向 将上一个快照
#将HEAD移动后指向的快照回滚到暂存区

git reset --soft HEAD~ 

#移动HEAD的指向 将上一个快照  相当于撤销上一次提交

git reset --hard HEAD~

#移动HEAD的指向 将上一个快照  相当于撤销上一次提交
#将HEAD移动后指向的快照回滚到暂存区域
#将暂存区的文件还原到工作目录
--soft 	#移动HEAD的指向
--mixed	#将快照回滚到暂存区
--hard	#将暂存区还原到工作目录
```


```shell
#回滚指定快照  回滚个别文件
#指定快照ID	
git reset  文件SHA1哈希值（版本快照ID号）
```

?	

## 第四课

```shell
#创建工作文件夹 MyProject2 

#创建项目跟踪	
git init  

#创建README.md文件
touch README.md

#提交入暂存区	
git add 文件 	

#提交项目	
git commit -m "注释"
```

  	

```shell
#修改工作区内的文件内容
#比较工作区文件和暂存区文件	
git diff 

	index 旧文件ID  新文件ID    旧文件权限新文件权限
	---	为暂存区旧文件
	+++	为工作区新文件

	带+号为新文件特有的

	J K 上下键  
	F向下翻页   D向下翻半页 U 向上翻半页

	g 跳转到最后一行  
	G 跳转到第一行

	3  g   跳转到第三行

	/ 从上往下搜索
	？从下往上搜索
	n 下一个匹配字

	h 进入帮助文档
	q 退出

#比较仓库中不同的历史快照
git diff 快照1的ID  快照2的ID
```


```shell
#比较工作区中和仓库中的快照
git diff 快照ID    	
git diff HEAD
```

```shell
#比较暂存区中和仓库中的快照
git diff --cached 	  	#（比较仓库最新快照）
git diff --cached  ID	#（比较仓库指定快照）
```

?	

## 第五课

```shell
#两种情况：
#1 版本刚提交到仓库，发现漏掉两个文件没有添加
#2 版本提交发现版本说明写的不够全面 无法显示修改意义

#修改最后一次提交 
#执行带 --amend 选项的 commit 提交命令
#GIT就会更正最近一次提交
git commit --amend  --m "说明"

#进入新界面修改提交说明
#按下 i 键  开始添加     backspace删除文本
#ESC推出编辑模式   
#shift加两下Z  保存推出
#:q! 不保存退出

#将快照中的文件恢复到工作区
git checkout -- README.md

#删除工作区和暂存区某个文件 （取消跟踪 下次提交不进入仓库） 
git rm 文件名		

#将指针恢复到上个快照 撤销上一次提交
git checkout HEAD~

#强制删除 暂存区 和 工作目录的文件
git rm -f 文件名

#仅仅删除暂存区文件  保留工作区文件
git rm --cached 文件名

#重命名文件
git mv 旧名 新名

#结合三步 
ren/mv 	旧名 新名
git rm 	旧名
git add 新名
```

## 第六课


	#创建分支
	git branch 分支名称


```shell
#查看一下 
git log --decorate --oneline 
	--decorate #显示所有指向快照的引用
	--oneline #简介显示	
	--graph #图像化显示
	--all #显示所有分支

git log --decorate --oneline --graph --all

#切换分支
git checkout 分支名称
```

## 第七课


```shell
#实际开发分支 
#	master		发布分支
#	hotfix		BUG修复分支
#	release		功能集合编译
#	develop		开发测试分支
#	feature		功能开发区

#合并分支
git merge 分支名称

#当两个分支都有同名且都修改过的文件  发生 冲突

#修改文件名 
git mv 旧名 新名	

#创建并还原到分支
git checkout -b 分支名称

#删除分支 
git branch -d 分支名称
```


?	远程
```shell
#修改远程仓库的本地别名
git remote rename oldname newname 
#移除与远程仓库的连接
git remote rm old_reposity_name 
#新增仓库   origin为默认 可以改为其他名称
git remote add origin git_remote_address
git remote add github git@github.com:User/RepoName.git
git remote add gitee git@gitee.com:User/RepoName.git
 
```

远程推送


```shell
#推送到 origin 别名连接的远程仓库 中 的 master 分支  
# -u 参数   把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来 可以简化命令
git push -u origin master
```

 

## 第八课

```sh
#匿名分支 
#用于实验

#reset 默认只将指定的文件恢复到暂存区 
#reset 无法在使用了 --soft 和 --hard 后再指定文件

#checkout 同时覆盖暂存区和工作区

#reset 命令家移动HEAD指针（--soft） 
#-> 覆盖暂存区（--mixed，默认）
#-> 覆盖工作区（--hard）

#checkout 切换指针 然后 覆盖暂存区和工作区

#相对于reset --hard 来说 checkout 命令更加安全，
#checkout在切换分之前会检查当前工作状态
#如果不是“clean”的话 GIT不会允许执行操作 
#而  reset --hard 则覆盖所有数据
```




















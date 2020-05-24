
# windows+Linux开发环境搭建

## Linux环境配置

### 1.IP配置

* 文件：/etc/sysconfig/network-scripts/ifcfg-ens33

```shell
  ONBOOT=yes
  BOOTPROTO=none
  IPADDR=192.168.112.10   # ip
  NETMASK=255.255.255.0   # 子网掩码
  GATEWAY=192.168.112.2   # 网关
  DNS1=8.8.8.8            # DNS服务器
```

### 2.selinux配置

* 直接关闭(立马生效)

```bash
  setenforce 0  # 关闭
  getenforce    # 查看状态
```

* 文件：/etc/selinux/config

```bash
  SELINUX=disabled  # 重启linxu是自动关闭
```

### 3.yum源配置

* wget安装

```bash
  wget: yum install wget -y
```

* repo文件替换

```bash
  mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup # 备份
  wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo  #替换
```

* 清除缓存

```bash
  yum clean all  && yum makecache
```

* epel源更新

```bash
  yum install epel-release -y
```

## python环境配置

### 1.依赖安装

```bash
  yum groupinstall 'Development Tools' -y
  yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make   mysql-devel libffi-devel  gdbm-devel xz-devel  -y
```

### 2.python下载与安装

* 下载

```bash
  wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
  tar -zxvf  Python-3.6.5.tgz
```

* 安装

```bash
  cd Python-3.6.5
  ./configure --prefix=/usr/local/python3.6  --enable-shared
```

* 环境配置

```bash
  cp /usr/local/python3.6/lib/libpython3.6m.so.1.0 /usr/local/lib64
  cp /usr/local/python3.6/lib/libpython3.6m.so.1.0 /usr/lib64
```

* 软链接

```bash
  ln –s /usr/local/python3.6/bin/python3 /usr/bin/python3
  ln -s /usr/local/python3.6/bin/pip3 /usr/bin/pip3
```

* 虚拟环境工具virtualenv安装

```bash
  pip3 install virtualenv                                    # 安装
  ln /usr/local/python3.6/bin/virtualenv /usr/bin/virtualenv # 软链接
```

* virtualev 基本操作

```bash
  virtualev env1   # 创建虚拟环境
  source activate  # 进入虚拟环境
```

* 虚拟环境管理工具virtualenvwrapper安装

```bash
  pip3 install virtualenvwrapper
```

* 全局变量配置(~/.bashrc)

```shell
  if [ -f /usr/local/python3.6/bin/virtualenvwrapper.sh ]; then
      export WORKON_HOME=$HOME/.virtualenvs
      export VIRTUALENVWRAPPER_PYTHON=/usr/local/python3.6/bin/python3
      source /usr/local/python3.6/bin/virtualenvwrapper.sh
  fi
```

* virtualenvwrapper基本用法

```bash
  mkvirtualenv env --python=python2 # 创建虚拟环境(指定python版本)
  workon                            # 选择虚拟环境
  deactivate                        # 退出虚拟环境
  rmvirtualenv                      # 删除虚拟环境
```

## mysql安装(centos7默认是mariadb)

* 安装mysql

```bash
  yum install mariadb mariadb-server  -y
```

* 环境配置

```bash
  mysql -uroot -p                      # 进入mysql
  uninstall plugin validate_password;  # 禁用密码检查
  SET PASSWORD = PASSWORD('');         # 设置密码
  skip-grant-tables                    # 删除配置文件中
```

## nginx安装

* nginx安装

```bash
  yum install nginx -y
```

* nginx配置(/etc/nginx/conf.d/*.conf)

```bash
  server {
      listen 80;                                   # 端口监听
      server_name xxxx.xxxx.com;                   # 域名
      charset utf-8;
  
      location / {
          proxy_pass http://127.0.0.1:3001;
          proxy_redirect default;
       }
  
      location ~ \.action$ {
          rewrite /apps/log_webui/(.+)$ /$1 break; # 重定向
          proxy_pass http://127.0.0.1:3002;
          proxy_redirect default;
      }
  }
```

## node安装

* node安装

```bash
  yum install nodejs -y
```

* node版本控制工具安装

```bash
  npm install -g n
```

* node版本升级

```bash
  n stable
```

## 文件共享

* 直接挂载

```bash
  mount -t cifs -o username=........,password=........,vers=2.0  //192.168.56.1/share /home/share
```

* virtualBox文件挂载

```bash
  mount -t vboxsf share /home/share/
```

# 说明
> 运行nsis7zsample.exe会在当前目录生成**bastion_act1_ending.bk2**.
> **bastion_act1_ending.bk2**是由分卷***bastion_act1_ending.7z.001***和**bastion_act1_ending.7z.002**组成的

# 脚本说明
- 由于nsi自带的7z插件不支持分卷解压，所以使用了7za.exe来执行分卷解压
- 这样在打包的时候可以将资源单独打成7z分卷，然后和nis编译的exe一起发布即可.


# 测试
- 切换到当前目录，执行```7za.exe a bastion_act1_intro bastion_act1_intro.bk2 -v16m```创建分卷
- 运行```nsis7zsample.exe```执行解压，会在out生成```bastion_act1_intro.bk2```
#bink动画文件播放

- ###lua脚本
> moviesWidgets:PlayMovie('/bink/bastion_act1_intro.bk2')

- ### C++函数
```C++
void CMoviePanel::Play(const wstring& sFileName)
{
	MessageBoxW(NULL, sFileName.c_str(), sFileName.c_str(), NULL);
	if (m_hMovieHandle != INVALID_HANDLE)
	{
		if (sFileName.empty() || sFileName == m_sFileName)
		{
			Vid.BinkPlay(m_hMovieHandle);
			return;
		}
		else
			FinishMovie();
	}

	m_sFileName = sFileName.empty() ? m_sFileName : sFileName;
	wstring sPath(IResource::FindLocPath(m_sFileName, L""));
	sPath = FileManager.GetSystemPath(sPath);

	float fBinkAspect(0.0f);

	Vid.BinkCreateHandle(sPath, m_hMovieHandle, fBinkAspect);
```
> **sFileName：/bink/bastion_act1_intro.bk2**
> **sPath：D:/strife_us/ui_20150528/Strife/game/bink/bastion_act1_intro.bk2**

#动画资源的打包
- ###打包bink:BinkCreateHandle里最终会调用BinkOpen打开动画，但是zip包只适合相对路径，所以打包进去也找不到动画了。
- ###原有机制:bink目录单独存在，不支持升级

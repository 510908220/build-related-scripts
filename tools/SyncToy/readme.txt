Microsoft(r) SyncToy 2.1

=======
Read Me
=======

Table Of Contents:
------------------
1.1 SyncToy Overview
1.2 What Does SyncToy Do?
1.3 What's So Special About SyncToy?
1.4 How Does SyncToy Deliver These Benefits?
1.5 What's New in SyncToy 2.1
1.6 Installation Notes


1.1 SyncToy Overview
--------------------

SyncToy can help you synchronize, copy, backup and maintain folders of files on your 
computers.


1.2 What Does SyncToy Do?
-------------------------

SyncToy synchronizes the files in folders of your choosing. It does so by copying, 
renaming, and deleting files. 


1.3 What's So Special About SyncToy?
-------------------------------------

There are many ways to copy files in a Windows® environment. However, SyncToy is faster, 
easier to configure, more transparent, and easier to repeat than: 
- Using Drag and Drop from Windows Explorer, 
- Using Copy or XCopy from the command line, 
- Building batch files and/or scripts to automate file copy operations, 
- Using offline folders, or 
- Using Windows Briefcase. 


1.4 How Does SyncToy Deliver These Benefits?
--------------------------------------------

SyncToy helps you save time, minimize network usage, and save disk space by only copying 
when necessary. 

The simple, fast, and familiar Windows interface lets you point and click to define your 
folders and the SyncToy actions you want performed on each folder pair. You choose the 
appropriate action when you create a folder pair, and the action determines how SyncToy 
handles file conflicts such as: 

- Files that have been renamed in both folders, 
- Files deleted from one folder and renamed in the other, 
- Files renamed in one folder and modified in the other, and  
- Many other file conflict situations. 

SyncToy enables you to save how you want your folder pairs synced so you can sync again 
and again with a single click of a button. 

SyncToy lets you sync a single pair of folders or all of your folder pairs with a single 
click. You can even set up SyncToy to run unattended. 

The powerful preview feature in SyncToy shows you exactly what is going to happen before 
any files are touched. Preview even gives you a chance to unselect any proposed actions 
before you start. 


1.5 What's New in SyncToy 2.1
-----------------------------

The following features were added to this release of SyncToy: 

- Dynamic Drive Letter Assignment: Drive letter reassignment will now be detected and 
  updated in the folder pair definition. 
- True Folder Sync: Folder creates, renames and deletes are now synchronized for all 
  SyncToy actions. 
- Exclusion Filtering Based on Name: File exclusion based on name with exact or fuzzy 
  matching. 
- Filtering Based on File Attributes: The ability to exclude files based on one or more 
  file attributes (Read-Only, System, Hidden). 
- Unattended Folder Pair Execution: Addressed issues related to running scheduled 
  folder pairs while logged off. 
- Folder Pairs With Shared Endpoints: Ability for folder pairs associated with the 
  same or different instances of SyncToy to share end-points. 
- Command line enhancements: Added the ability to manage folder pairs via the command 
  line interface. 
- Re-Architect Sync Engine: 
     - The SyncToy engine has been rearchitected to provide scalability and the ability 
       to add significant enhancements in future releases. 
     - Sync engine is also more robust insomuch that many single, file level errors are  
       skipped without affecting the entire sync operation. 
- Sync Encrypted Files: Sync of Encrypted files works when local folder and files are 
  encrypted, which addresses the common scenario involving sync between local, encrypted 
  laptop PC folder and remote, unencrypted desktop PC folder. 
- 64-Bit Support: SyncToy now has a native 64-bit build (x64 only) for 64-bit versions 
  of Windows. 
- Folder pair rename 
- Sub-folder Exclusion Enhancements: Descendents created under excluded sub-folders are 
  automatically excluded. Usability improvements for the sub-folder exclusion dialog. 
- Folder Pair Metadata Moved: Folder pair metadata removed from MyDocuments to resolve 
  any issues with server-based folder pair re-direction setup. 
- Setup Improvements: Integrated setup with single self-extracting archive file and no 
  extra downloads if you already have .NET Framework 2.0 installed. Enabled silent 
  install for the SyncToy Installer file (see readme.txt file for more information). 
- Removed combine and subscribe actions. 


1.6 Installation Notes
----------------------

Upgrade:

- If upgrading from an earlier version of SyncToy (e.g. SyncToy 1.4 or SyncToy 2.0 Beta), 
  it is **CRITICAL** to ensure that all folder pairs are fully synchronized using the 
  previous version before running SyncToy 2.1 setup. Not following this guideline can 
  lead to unintended behavior and partial data loss when running SyncToy 2.1 for the 
  first time after upgrade. All folder pairs must also be fully synchronized at least 
  once right after the upgrade is done. 

Installation:

- Both 32-bit and 64-bit versions of SyncToy are available as a single self-extracting 
  archive executable which runs all of the required setup components when launched. 
  The 64-bit version is targeted to 64-bit versions of Windows, e.g. Windows XP x64 Edition 
  or Windows Vista 64-bit editions. 
- The 32-bit version may be installed and run on a 64-bit version of Windows as well. 
- Simultaneous side-by-side installation of the 32-bit and 64-bit versions on the same 
  machine is not recommended or supported.
- SyncToy supports quiet installation by an Administrator user on the target machine. 
  The steps for this are as follows. Please download the self-extracting archive 
  executable and save locally. Extract files from the archive to a target directory. 
  You'll notice 3 MSI files in the set of extracted files. Each of the 3 MSIs can be run 
  in quiet mode using the MSI command line utility (msiexec.exe). The order in which the 
  MSIs need to be installed is: Synchronization-v2.0-{x64/x86}-ENU.msi.msi, ProviderServices-v2.0-{x64/x86}-ENU.msi, 
  SyncToySetup.msi.

Other Notes:

- SyncToy depends on components of the Microsoft Sync Framework which are included in 
  SyncToy setup in case they are not already installed on the target machine. Installing  
  SyncToy along with the dependent components requires the use of an account with 
  Administrator privileges on the target machine. If the Microsoft Sync Framework components 
  are already installed on the target machine, SyncToy can be installed from a 
  non-administrator user account.
- The SyncToy application will stop working if any of the dependent components are 
  uninstalled, which can be fixed by re-running the full install package on the target machine.
- If SyncToy 2.1 is installed using an account which is different than the one that  was used 
  to install previous versions of SyncToy, then the previous version will not be uninstalled.  
  In this case, it is recommended that users uninstall the previous version using the previously 
  used user account before installing SyncToy 2.1.
- If uninstalling SyncToy 2.1, the same user account must be used which was used for 
  installation.


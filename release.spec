<?xml version="1.0" encoding="UTF-8"?>
<spec>
	<config name="common" product="strife" branch="cn_prod" distname="Strife">
		<search path="/base" />
		<search path="/game" />
		<search path="/" recurse="false" />
		<ignore expression="*.tga;*.sources;*.atlas;/game/test/*;/game/dev_heroes/*;*.pdb;*.wav;*.texture;*.cvsignore;*.dlu;/dxwebsetup.exe;/tmodel.exe;/bin/update_generator.exe;/bin/strife.exp;/bin/strife.lib;/bin/strife_dumpuploader.exe;/bin/strife_twitch.exe;*.psd;*.max;/game/svr_master_request_dump.txt" />
		<unignore expression="/game/core/cursors/*.tga" />
		<archive name="resources0" mod="game" include="*" exclude="*.bk2" />
		<archive name="resources0" mod="base" include="*" exclude="" />
		<textfiles expression="*.str;*.txt;*.lua;*.cfg;*.set;*.xsd" />
		<textfiles expression="*.entity;*.effect;*.material;*.interface;*.package;*.resources;*.mdf;*.shader;*.node;*.cursor;*.itembuild;*.gamemechanics;*.economechanics;*.upgrades;*.botmetadata;*.bot" />
		<textfiles expression="*.entitylist;*.materiallist;*.soundlist;*.terrainmateriallist;*.texturelist;*.world;*.worldenvironmentregionlist;*.worldgameplayregionlist;*.worldoccluderlist" />
		<encrypt expression="/bin/*" />
	</config>

	<config name="servercommon" product="strife" branch="cn_prod" distname="Strife">
		<search path="/base" />
		<search path="/game" />
		<search path="/" recurse="false" />
		<ignore expression="*.tga;*.sources;*.atlas;/game/test/*;*.wav;*.texture;*.cvsignore;*.dlu;/dxwebsetup.exe;/tmodel.exe;*.psd;*.max;/game/svr_master_request_dump.txt" />
		<unignore expression="" />
		<archive name="resources0" mod="game" include="*" exclude="" />
		<archive name="resources0" mod="base" include="*" exclude="" />
		<textfiles expression="*.str;*.txt;*.lua;*.cfg;*.set;*.xsd" />
		<textfiles expression="*.entity;*.effect;*.material;*.interface;*.package;*.resources;*.mdf;*.shader;*.node;*.cursor;*.itembuild;*.gamemechanics;*.economechanics;*.upgrades;*.botmetadata;*.bot" />
		<textfiles expression="*.entitylist;*.materiallist;*.soundlist;*.terrainmateriallist;*.texturelist;*.world;*.worldenvironmentregionlist;*.worldgameplayregionlist;*.worldoccluderlist" />
		<encrypt expression="/bin/*" />
	</config>
	
	<config name="server" build="server" distname="Server">
		<ignore expression="*/generated_files/*;*.ogg;*.wav;*.dds;*.tga;*/bink/*;*/ui/*;*/ui_dev/*;*/core/fonts/*;*/core/cursors/*;*.psd;*.png;"/>
		<encrypt expression="/bin/*" />
	</config>
	
	<config name="client" build="client">
		<!-- archive name="sounds" mod="game" include="*.ogg" />
		<archive name="textures" mod="game" include="*.dds" />
		<archive name="bastion" mod="game" include="/heroes/bastion/*;/generated_files/*/bastion/*" / -->
		<remap frompath="/game/generated_files" topath="/game" />
		<remap frompath="/base/generated_files" topath="/base" />
	</config>
	
	<config name="linux" os="linux" distname="Linux">
		<ignore expression="*.dbg;/icon.ico;*.dlu;*.exe" />
		<exec expression="/bin/strife" />
		<exec expression="/bin/launcher" />
	</config>
	
	<config name="windows" os="windows" distname="Windows">
		<ignore expression="/icon.png" />
	</config>
	
	<config name="x86" arch="x86">
	</config>
	
	<config name="x64" arch="x64" distname="64">
	</config>
	
	<config name="universal" arch="universal">
	</config>
	
	<target name="server_linux" configs="common;server;linux;x64">
		<search path="bin64_linux_server" />
		<remap frompath="/bin64_linux_server" topath="/bin" />
	</target>

	<target name="linux" configs="common;client;linux;x86">
		<search path="bin_linux" />
		<remap frompath="/bin_linux" topath="/bin" />
	</target>
	
	<target name="linux64" configs="common;client;linux;x64">
		<search path="bin64_linux" remap="bin" />
		<remap frompath="/bin64_linux" topath="/bin" />
		<encrypt expression="/bin/*" />
	</target>
	
	<target name="server_windows" configs="servercommon;server;windows;x86">
		<search path="bin_server" />
		<remap frompath="/bin64_server" topath="/bin" />
	</target>
	
	<target name="windows" configs="common;client;windows;x86">
		<search path="/directxredist" />
		<search path="bin" />
		<search path="/updater" />
		
		<updater expression="/updater/*" />
		<updater expression="/bin/updater.exe" />
		<updaterbin expression="/bin/updater.exe" />
	</target>
	
	<target name="windows64" configs="common;client;windows;x64">
		<search path="/directxredist" />
		<search path="bin64" />
		<remap frompath="/bin64" topath="/bin" />
	</target>
</spec>

# TODO:
# - find (permanent) solution for https://bugs.launchpad.net/pld-linux/+bug/501593

%define	_version	1.5
# Spanish sounds lag behind
%define	es_version	1.4.27

Summary:	Core sounds for Asterisk
Name:		asterisk-sounds-core
Version:	%{_version}
Release:	1
License:	CC-BY-SA
Group:		Applications/Sound
URL:		http://www.asterisk.org/
Source0:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-alaw-%{_version}.tar.gz
# Source0-md5:	31091dd45e04a9dffe3355be995d3bce
Source1:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-g722-%{_version}.tar.gz
# Source1-md5:	97381dec2d1791b9940bdbcddcec29fc
Source2:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-g729-%{_version}.tar.gz
# Source2-md5:	c3c8994fd58cc5a980e932aca5d2bac8
Source3:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-gsm-%{_version}.tar.gz
# Source3-md5:	560136ab2fbe737efb204e45352cff95
Source4:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-siren7-%{_version}.tar.gz
# Source4-md5:	ba12827c7093cb6089b876e61d9465a0
Source5:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-siren14-%{_version}.tar.gz
# Source5-md5:	79b362743207296f48325c6f550248f9
Source6:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-sln16-%{_version}.tar.gz
# Source6-md5:	fa113450d50c4c7ef0245953be59bb27
Source7:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-ulaw-%{_version}.tar.gz
# Source7-md5:	bb1e5b78b460d7f303fe967ef89d42cf
Source8:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-wav-%{_version}.tar.gz
# Source8-md5:	fc8b3eb4724b7b87a8b530cc1ae54da5
Source10:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-alaw-%{es_version}.tar.gz
# Source10-md5:	8a54d1149adea26e57be5d6fda30bc14
Source11:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-g722-%{es_version}.tar.gz
# Source11-md5:	97acc2cf26ad133d56470b4959cfc666
Source12:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-g729-%{es_version}.tar.gz
# Source12-md5:	78a0eb3b4813fd35914c65a16385a54e
Source13:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-gsm-%{es_version}.tar.gz
# Source13-md5:	5d4fcba1b476d42f58f4b1e8416828d8
Source14:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-siren7-%{es_version}.tar.gz
# Source14-md5:	87930f88fdb906daa7580e418ef81e3e
Source15:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-siren14-%{es_version}.tar.gz
# Source15-md5:	e07dd8488b10589d5444d20ae1461bd8
Source16:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-sln16-%{es_version}.tar.gz
# Source16-md5:	d2da4fb3517ff4a41c6c2cf59dcb2dbb
Source17:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-ulaw-%{es_version}.tar.gz
# Source17-md5:	0695f90d4b6af271973a48282d8ec66d
Source18:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-wav-%{es_version}.tar.gz
# Source18-md5:	09bb1ef017fdb9a88547faeff40f6c66
Source20:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-alaw-%{_version}.tar.gz
# Source20-md5:	e387ddc68d0ba581049f56f36e4d560b
Source21:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-g722-%{_version}.tar.gz
# Source21-md5:	5118c63ab67926709cc39b67a147408b
Source22:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-g729-%{_version}.tar.gz
# Source22-md5:	c8006e9ec6fe9d5055930db2c8d026c5
Source23:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-gsm-%{_version}.tar.gz
# Source23-md5:	867ff25099d7a8b0124040fd5931d411
Source24:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-siren7-%{_version}.tar.gz
# Source24-md5:	700f3ea4232243c86131b95fbcb63157
Source25:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-siren14-%{_version}.tar.gz
# Source25-md5:	192c3f6b82b184ab04850271a5a2dddf
Source26:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-sln16-%{_version}.tar.gz
# Source26-md5:	f0ec92fa7321775ea75681863581e65c
Source27:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-ulaw-%{_version}.tar.gz
# Source27-md5:	6165a0a49193c588313c2357e05c281f
Source28:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-wav-%{_version}.tar.gz
# Source28-md5:	faa4a28958a40bc5527c3b95b06f18d1
BuildRequires:	iconv
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		sounds_dir	%{_datadir}/asterisk/sounds

%description
Core sound files for Asterisk.

%package en
Summary:	Core English sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0

%description en
Core English sound files for Asterisk.

%package en-alaw
Summary:	Core English ALAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-en = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description en-alaw
Core English ALAW sound files for Asterisk.

%package en-g722
Summary:	Core English G.722 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-en = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description en-g722
Core English G.722 sound files for Asterisk.

%package en-g729
Summary:	Core English G.729 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-en = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description en-g729
Core English G.729 sound files for Asterisk.

%package en-gsm
Summary:	Core English GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-en = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description en-gsm
Core English GSM sound files for Asterisk.

%package en-siren7
Summary:	Core English Siren7 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-en = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description en-siren7
Core English Siren7 sound files for Asterisk.

%package en-siren14
Summary:	Core English GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-en = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description en-siren14
Core English Siren14 sound files for Asterisk.

%package en-sln16
Summary:	Core English SLN16 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-en = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description en-sln16
Core English SLN16 sound files for Asterisk.

%package en-ulaw
Summary:	Core English ULAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-en = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description en-ulaw
Core English ULAW sound files for Asterisk.

%package en-wav
Summary:	Core English WAV sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-en = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description en-wav
Core English WAV sound files for Asterisk.

%package es
Version:	%{es_version}
Summary:	Core Spanish sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0

%description es
Core Spanish sound files for Asterisk.

%package es-alaw
Version:	%{es_version}
Summary:	Core Spanish ALAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{es_version}-%{release}
Provides:	asterisk-sounds-core = %{es_version}-%{release}

%description es-alaw
Core Spanish ALAW sound files for Asterisk.

%package es-g722
Version:	%{es_version}
Summary:	Core Spanish G.722 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{es_version}-%{release}
Provides:	asterisk-sounds-core = %{es_version}-%{release}

%description es-g722
Core Spanish G.722 sound files for Asterisk.

%package es-g729
Version:	%{es_version}
Summary:	Core Spanish G.729 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{es_version}-%{release}
Provides:	asterisk-sounds-core = %{es_version}-%{release}

%description es-g729
Core Spanish G.729 sound files for Asterisk.

%package es-gsm
Version:	%{es_version}
Summary:	Core Spanish GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{es_version}-%{release}
Provides:	asterisk-sounds-core = %{es_version}-%{release}

%description es-gsm
Core Spanish GSM sound files for Asterisk.

%package es-siren7
Version:	%{es_version}
Summary:	Core Spanish Siren7 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{es_version}-%{release}
Provides:	asterisk-sounds-core = %{es_version}-%{release}

%description es-siren7
Core Spanish Siren7 sound files for Asterisk.

%package es-siren14
Version:	%{es_version}
Summary:	Core Spanish Siren14 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{es_version}-%{release}
Provides:	asterisk-sounds-core = %{es_version}-%{release}

%description es-siren14
Core Spanish Siren14 sound files for Asterisk.

%package es-sln16
Version:	%{es_version}
Summary:	Core Spanish SLN16 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{es_version}-%{release}
Provides:	asterisk-sounds-core = %{es_version}-%{release}

%description es-sln16
Core Spanish SLN16 sound files for Asterisk.

%package es-ulaw
Version:	%{es_version}
Summary:	Core Spanish ULAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{es_version}-%{release}
Provides:	asterisk-sounds-core = %{es_version}-%{release}

%description es-ulaw
Core Spanish ULAW sound files for Asterisk.

%package es-wav
Version:	%{es_version}
Summary:	Core Spanish WAV sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{es_version}-%{release}
Provides:	asterisk-sounds-core = %{es_version}-%{release}

%description es-wav
Core Spanish WAV sound files for Asterisk.

%package fr
Version:	%{_version}
Summary:	Core English sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0

%description fr
Core French sound files for Asterisk.

%package fr-alaw
Summary:	Core French ALAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{_version}-%{release}
Provides:	asterisk-sounds-core = %{_version}-%{release}

%description fr-alaw
Core French ALAW sound files for Asterisk.

%package fr-g722
Summary:	Core French G.722 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{_version}-%{release}
Provides:	asterisk-sounds-core = %{_version}-%{release}

%description fr-g722
Core French G.722 sound files for Asterisk.

%package fr-g729
Summary:	Core French G.729 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{_version}-%{release}
Provides:	asterisk-sounds-core = %{_version}-%{release}

%description fr-g729
Core French G.729 sound files for Asterisk.

%package fr-gsm
Summary:	Core French GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{_version}-%{release}
Provides:	asterisk-sounds-core = %{_version}-%{release}

%description fr-gsm
Core French GSM sound files for Asterisk.

%package fr-siren7
Summary:	Core French Siren7 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{_version}-%{release}
Provides:	asterisk-sounds-core = %{_version}-%{release}

%description fr-siren7
Core French Siren7 sound files for Asterisk.

%package fr-siren14
Summary:	Core French Siren14 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{_version}-%{release}
Provides:	asterisk-sounds-core = %{_version}-%{release}

%description fr-siren14
Core French Siren14 sound files for Asterisk.

%package fr-sln16
Summary:	Core French SLN16 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{_version}-%{release}
Provides:	asterisk-sounds-core = %{_version}-%{release}

%description fr-sln16
Core French SLN16 sound files for Asterisk.

%package fr-ulaw
Summary:	Core French ULAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{_version}-%{release}
Provides:	asterisk-sounds-core = %{_version}-%{release}

%description fr-ulaw
Core French ULAW sound files for Asterisk.

%package fr-wav
Summary:	Core French WAV sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{_version}-%{release}
Provides:	asterisk-sounds-core = %{_version}-%{release}

%description fr-wav
Core French WAV sound files for Asterisk.

%prep
%setup -qcT

if [ -f /proc/$PPID/environ ]; then
	# import env from parent process
	unset LC_ALL
	export $(tr '\0' '\n' < /proc/$PPID/environ | grep -E '^(LC_|LANG)')
	if locale | grep -Eqi 'utf-?8'; then
		echo >&2 "You should re-run rpmbuild with LANG=C LC_ALL=C, see https://bugs.launchpad.net/pld-linux/+bug/501593"
		exit 1
	fi
fi

for file in %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8}; do
	tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/!' > `basename $file .tar.gz`.list
	tar --extract --directory . --file $file
done

mkdir es
for file in %{S:10} %{S:11} %{S:12} %{S:13} %{S:14} %{S:15} %{S:16} %{S:17} %{S:18}; do
	tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/es/!' > `basename $file .tar.gz`.list
	tar --extract --directory ./es/ --file $file
done

mkdir fr
for file in %{S:20} %{S:21} %{S:22} %{S:23} %{S:24} %{S:25} %{S:26} %{S:27} %{S:28}; do
	tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/fr/!' > `basename $file .tar.gz`.list
	tar --extract --directory ./fr/  --file $file
done

iconv -f iso-8859-1 -t utf-8 < fr/core-sounds-fr.txt > fr/core-sounds-fr.txt.tmp
touch --reference fr/core-sounds-fr.txt fr/core-sounds-fr.txt.tmp
mv fr/core-sounds-fr.txt.tmp fr/core-sounds-fr.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{sounds_dir}/{,es,fr}

for file in $(cat *.list | sed -e 's!^%{sounds_dir}/!!'); do
	install -d $RPM_BUILD_ROOT%{sounds_dir}/$(dirname $file)
	cp -p $file $RPM_BUILD_ROOT%{sounds_dir}/$file
done

%clean
rm -rf $RPM_BUILD_ROOT

%files en
%defattr(644,root,root,755)
%doc core-sounds-en.txt
%doc CHANGES-asterisk-core-en-%{_version}
%doc CREDITS-asterisk-core-en-%{_version}
%doc LICENSE-asterisk-core-en-%{_version}
%dir %{sounds_dir}/dictate
%dir %{sounds_dir}/digits
%dir %{sounds_dir}/followme
%dir %{sounds_dir}/letters
%dir %{sounds_dir}/phonetic
%dir %{sounds_dir}/silence

%files en-alaw -f asterisk-core-sounds-en-alaw-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-alaw-%{_version}.list

%files en-g722 -f asterisk-core-sounds-en-g722-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-g722-%{_version}.list

%files en-g729 -f asterisk-core-sounds-en-g729-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-g729-%{_version}.list

%files en-gsm -f asterisk-core-sounds-en-gsm-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-gsm-%{_version}.list

%files en-siren7 -f asterisk-core-sounds-en-siren7-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-siren7-%{_version}.list

%files en-siren14 -f asterisk-core-sounds-en-siren14-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-gsm-%{_version}.list

%files en-sln16 -f asterisk-core-sounds-en-sln16-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-sln16-%{_version}.list

%files en-ulaw -f asterisk-core-sounds-en-ulaw-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-ulaw-%{_version}.list

%files en-wav -f asterisk-core-sounds-en-wav-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-wav-%{_version}.list

%files es
%defattr(644,root,root,755)
%doc es/core-sounds-es.txt
%doc es/CHANGES-asterisk-core-es-%{es_version}
%doc es/CREDITS-asterisk-core-es-%{es_version}
%doc es/LICENSE-asterisk-core-es-%{es_version}
%dir %{sounds_dir}/es
%dir %{sounds_dir}/es/dictate
%dir %{sounds_dir}/es/digits
%dir %{sounds_dir}/es/followme
%dir %{sounds_dir}/es/letters
%dir %{sounds_dir}/es/phonetic
%dir %{sounds_dir}/es/silence

%files es-alaw -f asterisk-core-sounds-es-alaw-%{es_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-alaw-%{es_version}.list

%files es-g722 -f asterisk-core-sounds-es-g722-%{es_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-g722-%{es_version}.list

%files es-g729 -f asterisk-core-sounds-es-g729-%{es_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-g729-%{es_version}.list

%files es-gsm -f asterisk-core-sounds-es-gsm-%{es_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-gsm-%{es_version}.list

%files es-siren7 -f asterisk-core-sounds-es-siren7-%{es_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-siren7-%{es_version}.list

%files es-siren14 -f asterisk-core-sounds-es-siren14-%{es_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-siren14-%{es_version}.list

%files es-sln16 -f asterisk-core-sounds-es-sln16-%{es_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-sln16-%{es_version}.list

%files es-ulaw -f asterisk-core-sounds-es-ulaw-%{es_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-ulaw-%{es_version}.list

%files es-wav -f asterisk-core-sounds-es-wav-%{es_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-wav-%{es_version}.list

%files fr
%defattr(644,root,root,755)
%doc fr/core-sounds-fr.txt
%doc fr/CHANGES-asterisk-core-fr-%{_version}
%doc fr/CREDITS-asterisk-core-fr-%{_version}
%doc fr/LICENSE-asterisk-core-fr-%{_version}
%dir %{sounds_dir}/fr
%dir %{sounds_dir}/fr/dictate
%dir %{sounds_dir}/fr/digits
%dir %{sounds_dir}/fr/followme
%dir %{sounds_dir}/fr/letters
%dir %{sounds_dir}/fr/phonetic
%dir %{sounds_dir}/fr/silence

%files fr-alaw -f asterisk-core-sounds-fr-alaw-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-alaw-%{_version}.list

%files fr-g722 -f asterisk-core-sounds-fr-g722-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-g722-%{_version}.list

%files fr-g729 -f asterisk-core-sounds-fr-g729-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-g729-%{_version}.list

%files fr-gsm -f asterisk-core-sounds-fr-gsm-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-gsm-%{_version}.list

%files fr-siren7 -f asterisk-core-sounds-fr-siren7-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-siren7-%{_version}.list

%files fr-siren14 -f asterisk-core-sounds-fr-siren14-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-siren14-%{_version}.list

%files fr-sln16 -f asterisk-core-sounds-fr-sln16-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-sln16-%{_version}.list

%files fr-ulaw -f asterisk-core-sounds-fr-ulaw-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-ulaw-%{_version}.list

%files fr-wav -f asterisk-core-sounds-fr-wav-%{_version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-wav-%{_version}.list

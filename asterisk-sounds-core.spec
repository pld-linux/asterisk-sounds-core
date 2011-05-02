# TODO:
# - find (permanent) solution for https://bugs.launchpad.net/pld-linux/+bug/501593
Summary:	Core sounds for Asterisk
Name:		asterisk-sounds-core
Version:	1.4.21
Release:	1
License:	CC-BY-SA
Group:		Applications/Sound
URL:		http://www.asterisk.org/
Source0:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-alaw-%{version}.tar.gz
# Source0-md5:	2f8f123059d0473448369c45bf302d4c
Source1:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-g722-%{version}.tar.gz
# Source1-md5:	d2f75130060b980b50cabc918e7a1feb
Source2:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-g729-%{version}.tar.gz
# Source2-md5:	4b25c312dbcf4b78b1395be2af31364f
Source3:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-gsm-%{version}.tar.gz
# Source3-md5:	f3236af6dce4978abbd721bc4a5229c5
Source4:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-siren7-%{version}.tar.gz
# Source4-md5:	796ec9fdff9522e7f12841fd862b134b
Source5:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-siren14-%{version}.tar.gz
# Source5-md5:	e070a4e6746a2baf27f4e349868807ed
Source6:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-sln16-%{version}.tar.gz
# Source6-md5:	bb061ce31c0228684e3ee772153e0120
Source7:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-ulaw-%{version}.tar.gz
# Source7-md5:	5dbbaadcc41e4b14325649caf8e7fb85
Source8:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-wav-%{version}.tar.gz
# Source8-md5:	c1d5a75be4683dc21c005414df591728
Source10:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-alaw-%{version}.tar.gz
# Source10-md5:	6f8964bbfd66841d9a9ead3cc68ef5c5
Source11:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-g722-%{version}.tar.gz
# Source11-md5:	97cce709abc5f488aa9ea095dac9c739
Source12:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-g729-%{version}.tar.gz
# Source12-md5:	e3fa07be09d759c15acb0f04d1d619f3
Source13:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-gsm-%{version}.tar.gz
# Source13-md5:	e2ed66bf001b211c63dfb1cd2f0a9240
Source14:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-siren7-%{version}.tar.gz
# Source14-md5:	9067930e5e48852e67563e102677d362
Source15:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-siren14-%{version}.tar.gz
# Source15-md5:	bbabf68c04194a5c33cdd524b2c5d589
Source16:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-sln16-%{version}.tar.gz
# Source16-md5:	0150fc9250da66704405b17763363b45
Source17:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-ulaw-%{version}.tar.gz
# Source17-md5:	55a27faca07ab73f7cf67cd497fbbfc7
Source18:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-wav-%{version}.tar.gz
# Source18-md5:	d4cd582e4fcdb8e546572eb3e4206f48
Source20:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-alaw-%{version}.tar.gz
# Source20-md5:	3a01c76d575798baa27b89028af1dce2
Source21:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-g722-%{version}.tar.gz
# Source21-md5:	798937d9b51b4dbba2963ef19b1bf811
Source22:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-g729-%{version}.tar.gz
# Source22-md5:	0c7327eae462e8c755e97179b20006b5
Source23:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-gsm-%{version}.tar.gz
# Source23-md5:	0e19c7f9fcea328ca916bd8c27805278
Source24:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-siren7-%{version}.tar.gz
# Source24-md5:	a7a82ce36ae708ceedd2fb5a50f2810e
Source25:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-siren14-%{version}.tar.gz
# Source25-md5:	9feb704b839128b4df39ff29c24a5184
Source26:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-sln16-%{version}.tar.gz
# Source26-md5:	912db1cc19375612d10beb9157ceac7e
Source27:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-ulaw-%{version}.tar.gz
# Source27-md5:	cc09428e6f14bbad005bfe55c11f21e1
Source28:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-wav-%{version}.tar.gz
# Source28-md5:	90d79afe5db833db6820f0b464f182a8
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
Summary:	Core Spanish sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0

%description es
Core Spanish sound files for Asterisk.

%package es-alaw
Summary:	Core Spanish ALAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description es-alaw
Core Spanish ALAW sound files for Asterisk.

%package es-g722
Summary:	Core Spanish G.722 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description es-g722
Core Spanish G.722 sound files for Asterisk.

%package es-g729
Summary:	Core Spanish G.729 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description es-g729
Core Spanish G.729 sound files for Asterisk.

%package es-gsm
Summary:	Core Spanish GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description es-gsm
Core Spanish GSM sound files for Asterisk.

%package es-siren7
Summary:	Core Spanish Siren7 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description es-siren7
Core Spanish Siren7 sound files for Asterisk.

%package es-siren14
Summary:	Core Spanish Siren14 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description es-siren14
Core Spanish Siren14 sound files for Asterisk.

%package es-sln16
Summary:	Core Spanish SLN16 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description es-sln16
Core Spanish SLN16 sound files for Asterisk.

%package es-ulaw
Summary:	Core Spanish ULAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description es-ulaw
Core Spanish ULAW sound files for Asterisk.

%package es-wav
Summary:	Core Spanish WAV sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-es = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description es-wav
Core Spanish WAV sound files for Asterisk.

%package fr
Summary:	Core English sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0

%description fr
Core French sound files for Asterisk.

%package fr-alaw
Summary:	Core French ALAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description fr-alaw
Core French ALAW sound files for Asterisk.

%package fr-g722
Summary:	Core French G.722 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description fr-g722
Core French G.722 sound files for Asterisk.

%package fr-g729
Summary:	Core French G.729 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description fr-g729
Core French G.729 sound files for Asterisk.

%package fr-gsm
Summary:	Core French GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description fr-gsm
Core French GSM sound files for Asterisk.

%package fr-siren7
Summary:	Core French Siren7 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description fr-siren7
Core French Siren7 sound files for Asterisk.

%package fr-siren14
Summary:	Core French Siren14 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description fr-siren14
Core French Siren14 sound files for Asterisk.

%package fr-sln16
Summary:	Core French SLN16 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description fr-sln16
Core French SLN16 sound files for Asterisk.

%package fr-ulaw
Summary:	Core French ULAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

%description fr-ulaw
Core French ULAW sound files for Asterisk.

%package fr-wav
Summary:	Core French WAV sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-core-fr = %{version}-%{release}
Provides:	asterisk-sounds-core = %{version}-%{release}

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
%doc CHANGES-asterisk-core-en-%{version}
%doc CREDITS-asterisk-core-en-%{version}
%doc LICENSE-asterisk-core-en-%{version}
%dir %{sounds_dir}/dictate
%dir %{sounds_dir}/digits
%dir %{sounds_dir}/followme
%dir %{sounds_dir}/letters
%dir %{sounds_dir}/phonetic
%dir %{sounds_dir}/silence

%files en-alaw -f asterisk-core-sounds-en-alaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-alaw-%{version}.list

%files en-g722 -f asterisk-core-sounds-en-g722-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-g722-%{version}.list

%files en-g729 -f asterisk-core-sounds-en-g729-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-g729-%{version}.list

%files en-gsm -f asterisk-core-sounds-en-gsm-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-gsm-%{version}.list

%files en-siren7 -f asterisk-core-sounds-en-siren7-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-siren7-%{version}.list

%files en-siren14 -f asterisk-core-sounds-en-siren14-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-gsm-%{version}.list

%files en-sln16 -f asterisk-core-sounds-en-sln16-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-sln16-%{version}.list

%files en-ulaw -f asterisk-core-sounds-en-ulaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-ulaw-%{version}.list

%files en-wav -f asterisk-core-sounds-en-wav-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-en-wav-%{version}.list

%files es
%defattr(644,root,root,755)
%doc es/core-sounds-es.txt
%doc es/CHANGES-asterisk-core-es-%{version}
%doc es/CREDITS-asterisk-core-es-%{version}
%doc es/LICENSE-asterisk-core-es-%{version}
%dir %{sounds_dir}/es
%dir %{sounds_dir}/es/dictate
%dir %{sounds_dir}/es/digits
%dir %{sounds_dir}/es/followme
%dir %{sounds_dir}/es/letters
%dir %{sounds_dir}/es/phonetic
%dir %{sounds_dir}/es/silence

%files es-alaw -f asterisk-core-sounds-es-alaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-alaw-%{version}.list

%files es-g722 -f asterisk-core-sounds-es-g722-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-g722-%{version}.list

%files es-g729 -f asterisk-core-sounds-es-g729-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-g729-%{version}.list

%files es-gsm -f asterisk-core-sounds-es-gsm-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-gsm-%{version}.list

%files es-siren7 -f asterisk-core-sounds-es-siren7-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-siren7-%{version}.list

%files es-siren14 -f asterisk-core-sounds-es-siren14-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-siren14-%{version}.list

%files es-sln16 -f asterisk-core-sounds-es-sln16-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-sln16-%{version}.list

%files es-ulaw -f asterisk-core-sounds-es-ulaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-ulaw-%{version}.list

%files es-wav -f asterisk-core-sounds-es-wav-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-es-wav-%{version}.list

%files fr
%defattr(644,root,root,755)
%doc fr/core-sounds-fr.txt
%doc fr/CHANGES-asterisk-core-fr-%{version}
%doc fr/CREDITS-asterisk-core-fr-%{version}
%doc fr/LICENSE-asterisk-core-fr-%{version}
%dir %{sounds_dir}/fr
%dir %{sounds_dir}/fr/dictate
%dir %{sounds_dir}/fr/digits
%dir %{sounds_dir}/fr/followme
%dir %{sounds_dir}/fr/letters
%dir %{sounds_dir}/fr/phonetic
%dir %{sounds_dir}/fr/silence

%files fr-alaw -f asterisk-core-sounds-fr-alaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-alaw-%{version}.list

%files fr-g722 -f asterisk-core-sounds-fr-g722-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-g722-%{version}.list

%files fr-g729 -f asterisk-core-sounds-fr-g729-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-g729-%{version}.list

%files fr-gsm -f asterisk-core-sounds-fr-gsm-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-gsm-%{version}.list

%files fr-siren7 -f asterisk-core-sounds-fr-siren7-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-siren7-%{version}.list

%files fr-siren14 -f asterisk-core-sounds-fr-siren14-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-siren14-%{version}.list

%files fr-sln16 -f asterisk-core-sounds-fr-sln16-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-sln16-%{version}.list

%files fr-ulaw -f asterisk-core-sounds-fr-ulaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-ulaw-%{version}.list

%files fr-wav -f asterisk-core-sounds-fr-wav-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-core-sounds-fr-wav-%{version}.list

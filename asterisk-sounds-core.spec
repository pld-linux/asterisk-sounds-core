# TODO:
# - find (permanent) solution for https://bugs.launchpad.net/pld-linux/+bug/501593
Summary:	Core sounds for Asterisk
Name:		asterisk-sounds-core
Version:	1.4.17
Release:	2
License:	CC-BY-SA
Group:		Applications/Sound
URL:		http://www.asterisk.org/
Source0:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-alaw-%{version}.tar.gz
# Source0-md5:	bc8a0d9041e3ebd65fd6d6399f8a08e6
Source1:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-g722-%{version}.tar.gz
# Source1-md5:	0c20be63d2459a1d6f63c870a82c2657
Source2:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-g729-%{version}.tar.gz
# Source2-md5:	f453ed3e6d1b8954a12d43e219aef005
Source3:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-gsm-%{version}.tar.gz
# Source3-md5:	3fd0fce5ce43b028ff99aea60262b75d
Source4:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-siren7-%{version}.tar.gz
# Source4-md5:	5bf72fc0954e287674aff3aca67c0888
Source5:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-siren14-%{version}.tar.gz
# Source5-md5:	9a76765fff87b702cc5f2cf9c4c44a2e
Source6:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-sln16-%{version}.tar.gz
# Source6-md5:	42ba9cd1bb770d2a72d37ff7be0c4335
Source7:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-ulaw-%{version}.tar.gz
# Source7-md5:	5c6eb4fe64076c1106857834c59b2af1
Source8:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-wav-%{version}.tar.gz
# Source8-md5:	ed8c33aed4cd33cbc2b5db126d05cd0e
Source10:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-alaw-%{version}.tar.gz
# Source10-md5:	b0e8b6f39564a0d5f6d65a15994d26e2
Source11:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-g722-%{version}.tar.gz
# Source11-md5:	e0d1ddd6704e6f09c02b9ec2b0c4d340
Source12:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-g729-%{version}.tar.gz
# Source12-md5:	8c515c13ea40061509a93e2a601e2aeb
Source13:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-gsm-%{version}.tar.gz
# Source13-md5:	618fce9e53e3da2e7355a1b6d37df94d
Source14:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-siren7-%{version}.tar.gz
# Source14-md5:	4f2d65211bf6c607403348a45511d8d4
Source15:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-siren14-%{version}.tar.gz
# Source15-md5:	ffe3bc356ff2b1760c961d5a7d217396
Source16:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-sln16-%{version}.tar.gz
# Source16-md5:	337e5fe779a33a47cb4bd7403865d1d0
Source17:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-ulaw-%{version}.tar.gz
# Source17-md5:	bb81ed607e78dfbe6e9682287fb564a3
Source18:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-wav-%{version}.tar.gz
# Source18-md5:	5973a86090c58cf963c3a59c74eac0e1
Source20:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-alaw-%{version}.tar.gz
# Source20-md5:	3a9debcf5d762e58d5ba4decd1f07185
Source21:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-g722-%{version}.tar.gz
# Source21-md5:	67189692bb924946fbf4ba45a42eaae1
Source22:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-g729-%{version}.tar.gz
# Source22-md5:	841b0fdcc7675abb42510f4cb1da956e
Source23:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-gsm-%{version}.tar.gz
# Source23-md5:	8befa8aad8f6733c65c3b6bb1849f4cf
Source24:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-siren7-%{version}.tar.gz
# Source24-md5:	4996d6fb080bf2e49aa1a8e5c184dd92
Source25:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-siren14-%{version}.tar.gz
# Source25-md5:	2e59f5bb5898d7f959610f17a2ce6a9b
Source26:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-sln16-%{version}.tar.gz
# Source26-md5:	be6246716405dc0980b151f4cd8994e3
Source27:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-ulaw-%{version}.tar.gz
# Source27-md5:	ce5b81e9c95a41ee73c79c68690213a8
Source28:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-wav-%{version}.tar.gz
# Source28-md5:	193ea9b43cdd52e5c72faeee9cc84b7e
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

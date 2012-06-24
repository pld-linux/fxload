Summary:	EZ-USB utility program
Summary(pl):	Narz�dzie dla chip�w EZ-USB
Name:		fxload
Version:	2002_04_11
Release:	1
Group:		Applications/System
License:	GPL
URL:		http://linux-hotplug.sourceforge.net/
Source0:	http://unc.dl.sourceforge.net/sourceforge/linux-hotplug/%{name}-%{version}.tar.gz
# Source0-md5:	cafd71a5bff0c57bcd248273b2541c05
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains utilities for downloading firmware to EZ-USB
devices. EZ-USB devices use 8051-based microcontrollers that have been
enhanced with registers, buffers, and other device-side support for
USB transactions.

It currently supports devices based on the Anchorchips EZ-USB, as well
as the Cypress EZ-USB FX (which is almost completely source
compatible) and EZ-USB FX2 (which is not). All of these support full
speed (12 Mbit/sec) transfers. The FX2 also supports high speed (480
Mbit/s) transfers, introduced in USB 2.0.

This version of FXLOAD supports optional use of two-stage loading,
where special device firmware is used to support writing into off-chip
memory such as RAM (when firmware neeeds more than about 8 KBytes of
code and data) or, for firmware development, I2C serial EEPROM.

%description -l pl
Ten pakiet zawiera narz�dzia do wgrywania oprogramowania do urz�dze�
EZ-USB. Urz�dzenia EZ-USB u�ywaj� mikrokontroler�w bazuj�cych na 8051
rozszerzonych o dodatkowe rejestry, bufory i inne rozszerzenia dla
transakcji USB.

Obecnie wspiera urz�dzenia bazuj�ce na Anchorchips EZ-USB jak r�wnie�
Cypress EZ-USB FX (kt�ry jest niemal kompletnie �r�d�owo
kompatybilny), a tak�e EZ-USB FX2 (kt�ry nie jest kompatybilny).
Wszystkie te chipy obs�uguj� transfery z pe�n� pr�dko�ci� (12Mbit/s).
Chip FX2 dodatkowo wspiera transfery wysokiej pr�dko�ci (480Mbit/s)
wprowadzone w USB 2.0.

Ta wersja FXLOAD opcjonalnie wspiera dwu-etapowe �adowanie, gdzie
specjalne firmware u�ywane jest do obs�ugi zapisywania do pami�ci
znajduj�cej si� poza chipem takiej jak RAM (w momencie gdy firmware
potrzebuje wi�cej ni� 8Kbajt�w kodu i danych) lub w przypadku
rozwijania firmware, I2C szeregowej EEPROM.

%prep
%setup -q

%build
%{__make} all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DFXLOAD_VERSION=\\\"%{version}\\\""

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) /sbin/*
%{_mandir}/man?/*
%{_datadir}/usb/*.hex

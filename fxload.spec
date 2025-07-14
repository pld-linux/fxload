Summary:	EZ-USB utility program
Summary(pl.UTF-8):	Narzędzie dla układów EZ-USB
Name:		fxload
Version:	2008_10_13
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/linux-hotplug/%{name}-%{version}.tar.gz
# Source0-md5:	4477a2457f064228bef4a93ba2f21692
Patch0:		%{name}-link.patch
Patch1:		%{name}-firmwaredir.patch
URL:		http://linux-hotplug.sourceforge.net/
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

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do wczytywania oprogramowania do urządzeń
EZ-USB. Urządzenia EZ-USB używają mikrokontrolerów opartych na 8051
rozszerzonych o dodatkowe rejestry, bufory i inne rozszerzenia dla
transakcji USB.

Obecnie obsługuje urządzenia parte na Anchorchips EZ-USB jak również
Cypress EZ-USB FX (który jest niemal całkowicie zgodny na poziomie
źródeł), a także EZ-USB FX2 (który nie jest kompatybilny). Wszystkie
te układy obsługują transfery z pełną prędkością (12Mbit/s). Układ FX2
dodatkowo obsługuje transfery wysokiej prędkości (480Mbit/s),
wprowadzone w USB 2.0.

Ta wersja FXLOAD opcjonalnie obsługuje ładowanie dwuetapowe, w którym
specjalne firmware używane jest do obsługi zapisywania do pamięci
znajdującej się poza układem, takiej jak RAM (w momencie gdy firmware
potrzebuje więcej niż 8 kilobajtów kodu i danych) lub, w przypadku
rozwijania firmware, EEPROM dostępnej przez I2C.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -DFXLOAD_VERSION=\\\"%{version}\\\"" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) /sbin/fxload
%{_mandir}/man8/fxload.8*
/lib/firmware/ezusb

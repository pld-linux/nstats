Summary:	A traffic Analyser
Summary(pl.UTF-8):	Analizator ruchu w sieci
Name:		nstats
Version:	0.4
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://trash.net/~reeler/nstats/files/%{name}-%{version}.tar.gz
# Source0-md5:	92e737781d918ae68fd27b5fa16d5dec
URL:		http://reeler.org/nstats/
Conflicts:	bmon
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nstats prints statistics about ethernet network traffic. This includes
protocol breakdown on several layers, counting packets and bytes per
protocol, average packet size per protocol, TOS statistics, and TCP
options usage.

%description -l pl.UTF-8
nstats pokazuje statystyki ruchu w sieciach ethernetowych. Obejmuje to
różnorakie awarie protokołu na kilku warstwach, zliczanie pakietów i
bajtów per protokół, średni rozmiar pakietu per protokół, statystyki
TOS oraz użycie opcji TCP.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nstats
%attr(755,root,root) %{_bindir}/bmon
%attr(755,root,root) %{_bindir}/cmon
%attr(755,root,root) %{_bindir}/nmon
%{_mandir}/man8/nstats.8.gz

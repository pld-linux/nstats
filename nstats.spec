Summary:	A traffic Analyser
Summary(pl):	Analizator ruchu w sieci
Name:		nstats
Version:	0.4
Release:	0.1
License:	GPL
Group:		Networking
URL:		http://reeler.org/nstats/
Source0:	http://trash.net/~reeler/nstats/files/%{name}-%{version}.tar.gz
# Source0-md5:	92e737781d918ae68fd27b5fa16d5dec
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

nstats prints statistics about ethernet network traffic. This includes
protocol breakdown on several layers, counting packets and bytes per
protocol, average packet size per protocol, TOS statistics, and TCP
options usage.

%description -l pl

nstats pokazuje statystyki ruchu w sieciach ethernetowych.

%prep
%setup -q
%build
%configure
%{__make} CFLAGS="-I/usr/include/ncurses"
%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(644,root,root,755)
%doc %{_mandir}/man8/nstats.8.gz
%attr(0700,root,root) %{_bindir}/nstats
%attr(0700,root,root) %{_bindir}/bmon
%attr(0700,root,root) %{_bindir}/cmon
%attr(0700,root,root) %{_bindir}/nmon

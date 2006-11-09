Summary:	CHR - Character Handling Routines
Summary(pl):	CHR - funkcje do obs³ugi znaków
Name:		starlink-chr
Version:	2.2_5.218
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/chr/chr.tar.Z
# Source0-md5:	6a611003114e8e850f94e0dd200c8421
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_CHR.html
BuildRequires:	gcc-g77
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-cnf-devel
BuildRequires:	starlink-sae-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
The CHR library augments the limited character handling facilities
provided by the Fortran 77 standard. It offers a range of character
handling facilities: from formatting Fortran data types into text
strings and the reverse, to higher level functions such as wild card
matching, string sorting, paragraph reformatting and justification.
The library may be used simply for building text strings for
interactive applications or as a basis for more complex text
processing applications.

%description -l pl
Biblioteka CHR zwiêksza ograniczone mo¿liwo¶ci obs³ugi znaków dostêpne
w standardzie Fortranu 77. Oferuje szeroki zakres mo¿liwo¶ci: od
formatowania fortranowych typów danych w ³añcuchy tekstowe i na odwrót
do funkcji wy¿szego poziomu, takich jak dopasowywanie masek,
sortowanie ³añcuchów, reformatowanie akapitów i justowanie. Biblioteka
mo¿e byæ u¿ywana po prostu do tworzenia ³añcuchów tekstu dla
interaktywnych aplikacji lub jako podstawa dla bardziej z³o¿onych
aplikacji do przetwarzania tekstu.

%package devel
Summary:	Header files for CHR library
Summary(pl):	Pliki nag³ówkowe biblioteki CHR
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for CHR library.

%description devel -l pl
Pliki nag³ówkowe biblioteki CHR.

%package static
Summary:	Static Starlink CHR library
Summary(pl):	Statyczna biblioteka Starlink CHR
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink CHR library.

%description static -l pl
Statyczna biblioteka Starlink CHR.

%prep
%setup -q -c

sed -i -e "s/ -O'/ %{rpmcflags} -fPIC'/;s/ ld -shared -soname / g77 -shared -Wl,-soname=/" mk

%build
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc chr.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/chr_dev
%attr(755,root,root) %{stardir}/bin/chr_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a

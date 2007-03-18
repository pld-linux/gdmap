# TODO:
# - fix pl translation
#
Summary:	A tool which allows to visualize disk space
Summary(pl.UTF-8):	Narzêdzie pozwalaj±ce wizualizowaæ zu¿cie przestrzeni dyskowej
Name:		gdmap
Version:	0.7.5
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gdmap/%{name}-%{version}.tar.gz
# Source0-md5:	e27f9a4c029449182ce5a4dbec38870e
URL:		http://gdmap.sourceforge.net
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GdMap is a tool which allows you to visualize disk space with one
single picture. To display directory structures, cushion treemaps are
used to visualize a complete folder or even the whole hard drive with
one picture.

%description -l pl.UTF-8
GdMap to narzêdzie które pozwala tobie zwizualizowaæ zu¿ycie
przestrzeni dyskowej na pojedynczym obrazku. Do wy¶wietlania struktury
katalogów u¿ywane s± PODUSZKOWE MAPY DRZEWA???. Pozwala to wizualizowaæ
pojedynczy katalog a nawet ca³e dyski na jednym obrazku.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang GdMap

%clean
rm -rf $RPM_BUILD_ROOT


%files -f GdMap.lang
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/*.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/*
%{_pixmapsdir}/*
%{_mandir}/man1/*

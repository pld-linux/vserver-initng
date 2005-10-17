Summary:	initng on vserver
Summary(pl):	initng dla vservera
Name:		vserver-initng
Version:	0.01
Release:	0.3
License:	GPL
Group:		Base
#Source0:	%{name}-rc
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	initng
Requires:	initng-pld
Requires:	util-linux
Requires:	vserver-basesystem
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
initng on vserver.

DO NOT install this package for a normal system!

%description -l pl
initng dla vservera.

NIE nale¿y instalowaæ tego pakietu na normalnym systemie!

%prep

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
You will need to setup '/sbin/initng' in
/etc/vservers/<vserver>/apps/init/cmd.start

and 'plain' in
/etc/vservers/<vserver>/apps/init/style
EOF
fi

%files
%defattr(644,root,root,755)

Summary:	initng on vserver
Summary(pl):	initng dla vservera
Name:		vserver-initng
Version:	0.0000.2
Release:	0.4
License:	GPL
Group:		Base
Source0:	%{name}-rc
Requires:	hdparm
Requires:	initng
Requires:	module-init-tools
Requires:	mount
Requires:	net-tools
Requires:	util-linux
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
install -d $RPM_BUILD_ROOT/etc/rc.d
install %{SOURCE0} $RPM_BUILD_ROOT/etc/rc.d/rc

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
cat << EOF

 **************************************************
 *                                                *
 *  	         BIG FAT WARNING!!!               *
 *                                                *
 *  This package is for use inside Vserver ONLY!  *
 *  DO NOT install it on normal system!           *
 *                                                *
 **************************************************

EOF
fi

%files
%defattr(644,root,root,755)
%dir /etc/rc.d
%attr(755,root,root) /etc/rc.d/rc

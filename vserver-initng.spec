Summary:	initng on vserver
Name:		vserver-initng
Version:	0.0000.2
Release:	0.4
License:	GPL
Group:		Base
Source0:	%{name}-rc
Requires:	initng
Requires:	mount
Requires:	util-linux
Requires:	net-tools
Requires:	hdparm
Requires:	module-init-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
TODO

DO NOT install this package for a normal system!

%prep

%build

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

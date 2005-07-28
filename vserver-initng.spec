Summary:	initng on vserver
Name:		vserver-initng
Version:	0.0000.1
Release:	0.6
License:	GPL
Group:		Base
Requires:	initng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
TODO

DO NOT install this package for a normal system!

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/{run/netreport,log}

for i in 0 1 2 3 4 5 6; do
	install -d $RPM_BUILD_ROOT/etc/rc.d/rc$i.d
done

cat <<'EOF' > $RPM_BUILD_ROOT/etc/rc.d/rc
#!/bin/sh
# avoid being interrupted by child or keyboard
trap : INT QUIT TSTP

echo "args: $#:$@"
runlevel="$1"
if [ "$runlevel" = 3 ]; then
	exec /sbin/initng --i_am_init &
	echo "initng execution failed!"
fi
EOF

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

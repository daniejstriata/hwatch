Name:           hwatch
Version:        0.3.15
Release:        3%{?dist}
Summary:        A modern alternative to the 'watch' command, it records differences in execution results and allows for examination of these differences afterward.
URL:            https://github.com/blacknon/hwatch/
License:        MIT
Source0:        https://github.com/blacknon/hwatch/archive/refs/tags/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  python3
BuildRequires:  curl
BuildRequires:  gcc

%define debug_package %{nil}

%description
hwatch is a alternative watch command. Records the results of command execution that can display its history and differences.

Features:
* Can keep the history when the difference, occurs and check it later.
* Can check the difference in the history. The display method can be changed in real time.
* Can output the execution result as log (json format).
* Custom keymaps are available.
* Support ANSI color code.
* Execution result can be scroll.
* Not only as a TUI application, but also to have the differences output as standard output.
* If a difference occurs, you can have the specified command additionally executed.

%prep
%setup -q

%build
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
$HOME/.cargo/bin/cargo build --release --all-features
strip target/release/%{name} 
sed -i 's/\r$//' completion/bash/%{name}-completion.bash

%install
install -D -m 644 completion/bash/%{name}-completion.bash %{buildroot}/etc/bash_completion.d/%{name}.bash
install -D -m 755 target/release/%{name} %{buildroot}/usr/bin/%{name}
install -D -m 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
install -D -m 644 README.md %{buildroot}/usr/share/doc/%{name}/README.md

%check
$HOME/.cargo/bin/cargo test --release --locked --all-features

%files
%license LICENSE
%doc README.md
/usr/bin/%{name}
/etc/bash_completion.d/%{name}.bash

%changelog
* Mon Oct 30 2024 Danie de Jager - 0.3.15-3
- Fixed bash completion by converting line endings.
* Mon Oct 28 2024 Danie de Jager - 0.3.15-2
* Sat May 29 2024 Danie de Jager - 0.3.15-1
* Mon May 13 2024 Danie de Jager - 0.3.14-2
 - strip binary
 - add bash completion
* Mon May 13 2024 Danie de Jager - 0.3.14-1
 - Initial version

# Source this after activating the venv if `doctor.py` says Java is too old:
#   source .venv/bin/activate
#   source tools/env.sh
#
# PySpark 4 needs Java 17+. macOS: pick the installed 17 JDK.

if command -v /usr/libexec/java_home >/dev/null 2>&1; then
  if JAVA_HOME_17=$(/usr/libexec/java_home -v 17 2>/dev/null); then
    export JAVA_HOME="$JAVA_HOME_17"
    export PATH="$JAVA_HOME/bin:$PATH"
  fi
fi

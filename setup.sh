unset PATH
for p in $baseInputs $buildInputs; do
    export PATH=$p/bin${PATH:+:}$PATH
done

function unpackPhase() {
  echo "unpackPhase"
}

function configurePhase() {
  echo "configurePhase"
}

function buildPhase() {
  echo "buildPhase"
}

function installPhase() {
  echo "installPhase"
}

function fixupPhase() {
    find $out -type f -exec patchelf --shrink-rpath '{}' \; -exec strip '{}' \; 2>/dev/null
}

function genericBuild() {
  echo "genericBuild"
}

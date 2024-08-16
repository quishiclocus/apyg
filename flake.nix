# in flake.nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        name = "simple";
        src = ./.;
        pkgs = nixpkgs.legacyPackages.${system};
        nativeBuildInputs = with pkgs; [(
          python312
        )];
        buildInputs = with pkgs; [
          (python312.withPackages (ps: [
            ps.pip
            ps.build
            ps.setuptools
          ]))
        ];
      in
      with pkgs;
      {
        devShells.default = mkShell {
          inherit buildInputs nativeBuildInputs;
        };
        packages.apyg =
          let
            version = "0.9.1";
            inherit (pkgs) stdenv lib;
          in
          stdenv.mkDerivation
            {
              inherit buildInputs nativeBuildInputs;
              name = "apyg-${version}";

              # https://nixos.wiki/wiki/Packaging/Binaries
              src = pkgs.fetchurl {
                url =
                  "https://github.com/quishiclocus/apyg/releases/download/0.9.1-2/apyg-0.9.1.tar.gz";
                sha256 = "sha256-r4BuwWFbQU5q0HVg82vELe/UyX9A788IOZkGDYBZpDc=";
              };

              preUnpack = ''
              '';

              unpackPhase = ''
              '';

              postUnpack = ''
              '';

              installPhase = ''
              '';

              preBuild = ''
              '';

              buildPhase = ''
                python -m build
              '';

              postBuild = ''
              '';

              outputs = [ "out" ];

              meta = with nixpkgs.lib; {
                homepage = "https://github.com/quishiclocus/apyg/";
                description =
                  "Generate random strings of varying length and complexity.";
              };
            };
      }
    );
}

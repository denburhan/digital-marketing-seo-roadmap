# Skill

Skill siap pakai untuk agen AI (format `SKILL.md` dengan frontmatter `name` dan `description`, dikenal oleh Claude Code, Hermes Agent, dan agen sejenis). Isinya generik dan tidak memuat data pribadi atau kredensial.

## Daftar
- `seo-playbook-id/`: riset keyword dan intent, audit halaman, diagnosis halaman tidak terindeks, dan penilaian klaim AI Search. Berbahasa Indonesia.
- `seo-playbook/`: versi Inggris dari skill yang sama (English version of the same skill).

## Pasang

Claude Code (skill pribadi):
```bash
git clone https://github.com/denburhan/digital-marketing-seo-roadmap.git
mkdir -p ~/.claude/skills
cp -r digital-marketing-seo-roadmap/skills/seo-playbook-id ~/.claude/skills/   # Indonesia
cp -r digital-marketing-seo-roadmap/skills/seo-playbook ~/.claude/skills/      # English
```

Hermes Agent:
```bash
cp -r digital-marketing-seo-roadmap/skills/seo-playbook-id ~/.hermes/skills/   # Indonesia
cp -r digital-marketing-seo-roadmap/skills/seo-playbook ~/.hermes/skills/      # English
```

Agen lain: salin folder `seo-playbook-id` ke direktori skill agen itu, atau tempel isi `SKILL.md` sebagai instruksi sistem.

## Cara memakai
Minta langsung, misalnya:
- "Audit halaman ini: <URL>, query target <query>."
- "Kelompokkan ekspor query Search Console ini jadi cluster dan petakan ke URL."
- "Halaman ini tidak terindeks, diagnosis urut."
- "Klaim ini soal AI Overview benar atau tidak?"

## Batasan
Skill tidak punya akses ke akunmu. Ia butuh data yang kamu berikan (ekspor Search Console, URL, hasil PageSpeed). Tanpa data, ia akan menulis N/A, bukan menebak.

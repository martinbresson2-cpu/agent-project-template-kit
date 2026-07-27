#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "README.md"
  "AGENTS.md"
  "PROMPT_START.md"
  "docs/roadmap/current_feature.md"
  "docs/roadmap/next_phase.md"
  "docs/fixes/fixes_log.md"
)

optional_files=(
  "docs/roadmap/archive.md"
  "docs/design/architecture.md"
  "docs/design/decisions.md"
  "docs/design/data_schema.md"
  "docs/product/vision.md"
  "docs/product/scope.md"
  "docs/workflow/agent_workflow.md"
  "docs/workflow/human_handoff.md"
)

missing_required=0

echo "Checking required files..."
for file in "${required_files[@]}"; do
  if [[ -f "$file" ]]; then
    echo "  [ok] $file"
  else
    echo "  [missing] $file"
    missing_required=1
  fi
done

echo
echo "Checking optional template files..."
for file in "${optional_files[@]}"; do
  if [[ -f "$file" ]]; then
    echo "  [present] $file"
  else
    echo "  [absent] $file"
  fi
done

echo
if [[ "$missing_required" -ne 0 ]]; then
  echo "Template check failed: one or more required files are missing."
  exit 1
fi

echo "Template check passed."
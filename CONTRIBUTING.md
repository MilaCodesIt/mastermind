# Contributing to Mastermind

Thank you for considering contributing! We welcome contributions from the community.

## Code of Conduct

Be respectful, inclusive, and constructive in all interactions.

## Getting Started

### Prerequisites
- Node.js 20+
- pnpm 8+
- Git

### Setup

```bash
git clone https://github.com/GlacierEQ/mastermind.git
cd mastermind
pnpm install
pnpm build
```

## Development Workflow

1. Create a branch: `git checkout -b feature/your-feature`
2. Make changes and commit: `git commit -m "feat: add awesome feature"`
3. Test: `pnpm test && pnpm build`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

## Adding a New Agent

Agents are the core of Mastermind. See [docs/agents/](docs/agents/) for detailed guide.

## Code Style

- Use TypeScript strict mode
- Prefer `const` over `let`
- Use arrow functions
- Document complex logic
- Use meaningful variable names

## Commit Messages

Use conventional commits:
- `feat: add feature description`
- `fix: fix bug description`
- `docs: update documentation`
- `test: add or update tests`

## Areas for Contribution

### High Priority
- New agent types
- Language support (Go, Rust, Python)
- Additional integrations
- Performance optimizations

### Community Contributions
- Bug fixes
- Documentation improvements
- Real-world use cases

---

Thank you for contributing! 🚀
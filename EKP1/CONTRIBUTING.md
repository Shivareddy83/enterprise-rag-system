# Contributing to Enterprise Knowledge Platform (EKP)

Thank you for your interest in contributing!

## Development Workflow

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/your-feature
```

3. Implement your changes.

4. Run tests

```bash
pytest
```

5. Format code

```bash
black backend/
ruff check backend/
```

6. Commit

```bash
git commit -m "feat: add document versioning"
```

7. Push

```bash
git push origin feature/your-feature
```

8. Open a Pull Request

---

## Coding Standards

- Follow PEP8
- Use type hints
- Write tests
- Update documentation
- No secrets in commits

---

## Pull Request Checklist

- Tests pass
- Documentation updated
- Code reviewed
- No merge conflicts

Thank you for contributing to EKP!
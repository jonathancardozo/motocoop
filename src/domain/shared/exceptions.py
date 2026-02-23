"""
Exceções customizadas do domínio
"""


class DomainException(Exception):
    """Exceção base do domínio"""
    pass


class EntityNotFoundException(DomainException):
    """Entidade não encontrada"""
    pass


class BusinessRuleViolationException(DomainException):
    """Regra de negócio violada"""
    pass


class InvalidStateTransitionException(DomainException):
    """Transição de estado inválida"""
    pass

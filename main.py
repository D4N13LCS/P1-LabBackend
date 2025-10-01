"""
Demonstração do uso da entidade Category com:
1. Criação de categorias
2. Serialização e reconstrução (to_dict / from_dict)
3. Atualização de atributos
4. Ativação e desativação
5. Registro e exibição de eventos de domínio

Este arquivo serve como um "guia prático" para mostrar como as
funcionalidades implementadas na entidade Category funcionam.
"""

from domain.category import Category


if __name__ == "__main__":
    print("=" * 60)
    print("PARTE 1 - CRIAÇÃO DE UMA CATEGORIA")
    print("=" * 60)

    cat = Category(name="Filmes", description="Categoria de filmes")
    print("Categoria criada com sucesso:")
    print(cat)

    print("\nEventos disparados até agora:")
    for e in cat.events:
        print(" -", e.__class__.__name__, e.__dict__)

    # ------------------------------------------------------------

    print("\n" + "=" * 60)
    print("PARTE 2 - SERIALIZAÇÃO E RECONSTRUÇÃO")
    print("=" * 60)

    # Serializando para dicionário
    data = cat.to_dict()
    print("Categoria serializada em dicionário:")
    print(data)

    # Reconstruindo a categoria a partir do dicionário
    new_cat = Category.from_dict(data)
    print("\nCategoria reconstruída a partir do dicionário:")
    print(new_cat)

    # ------------------------------------------------------------

    print("\n" + "=" * 60)
    print("PARTE 3 - ATUALIZAÇÃO DE ATRIBUTOS")
    print("=" * 60)

    print("Atualizando nome e descrição...")
    cat.update(name="Filmes de Ação", description="Categoria focada em ação")
    print("Categoria após atualização:", cat)

    print("\nEventos disparados até agora:")
    for e in cat.events:
        print(" -", e.__class__.__name__, e.__dict__)

    # ------------------------------------------------------------

    print("\n" + "=" * 60)
    print("PARTE 4 - DESATIVAÇÃO E ATIVAÇÃO")
    print("=" * 60)

    print(f"Status atual: {cat.is_active}")
    print("Desativando categoria...")
    cat.deactivate()
    print(f"Status depois de desativar: {cat.is_active}")

    print("\nReativando categoria...")
    cat.activate()
    print(f"Status depois de ativar: {cat.is_active}")

    print("\nEventos disparados até agora:")
    for e in cat.events:
        print(" -", e.__class__.__name__, e.__dict__)

    # ------------------------------------------------------------

    print("\n" + "=" * 60)
    print("PARTE 5 - LISTA FINAL DE EVENTOS")
    print("=" * 60)

    print("Todos os eventos registrados durante o ciclo de vida da categoria:")
    for idx, e in enumerate(cat.events, start=1):
        print(f"{idx}. {e.__class__.__name__} -> {e.__dict__}")

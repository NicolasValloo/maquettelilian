// ══════════════════════════════════════════════════════════════════
// Composant : sidebar — interactions collapse/expand + accordéon
// TypeScript car interaction complexe (animations, état, overlay)
// ══════════════════════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.getElementById('sidebar') as HTMLElement | null
  const overlay = document.getElementById('sidebar-overlay') as HTMLElement | null
  const toggleButton = document.getElementById('sidebar-toggle') as HTMLButtonElement | null
  const closeButton = document.getElementById('sidebar-close') as HTMLButtonElement | null

  if (!sidebar || !overlay || !toggleButton || !closeButton) return

  // ── Expand / Collapse ──

  function expand(): void {
    sidebar!.classList.add('sidebar--expanded')
    overlay!.classList.add('sidebar-overlay--active')
  }

  function collapse(): void {
    sidebar!.classList.remove('sidebar--expanded')
    overlay!.classList.remove('sidebar-overlay--active')
    // Fermer tous les accordéons quand la sidebar se ferme
    sidebar!.querySelectorAll('.sidebar__item--expanded').forEach((item) => {
      item.classList.remove('sidebar__item--expanded')
    })
  }

  toggleButton.addEventListener('click', () => {
    sidebar!.classList.contains('sidebar--expanded') ? collapse() : expand()
  })

  closeButton.addEventListener('click', collapse)
  overlay.addEventListener('click', collapse)

  document.addEventListener('keydown', (event: KeyboardEvent) => {
    if (event.key === 'Escape') collapse()
  })

  // ── Clic sur un lien en mode collapsé → expand ──

  sidebar.querySelectorAll('.sidebar__link').forEach((link) => {
    link.addEventListener('click', () => {
      if (!sidebar!.classList.contains('sidebar--expanded')) {
        expand()
      }
    })
  })

  // ── Accordéon : un seul ouvert à la fois ──

  sidebar.querySelectorAll<HTMLButtonElement>('[data-sidebar-accordion]').forEach((button) => {
    button.addEventListener('click', () => {
      if (!sidebar!.classList.contains('sidebar--expanded')) return

      const parent = button.closest('.sidebar__item') as HTMLElement | null
      if (!parent) return

      const wasExpanded = parent.classList.contains('sidebar__item--expanded')

      // Fermer tous les accordéons
      sidebar!.querySelectorAll('.sidebar__item--accordion.sidebar__item--expanded').forEach((item) => {
        item.classList.remove('sidebar__item--expanded')
      })

      // Ouvrir celui-ci si il n'était pas déjà ouvert
      if (!wasExpanded) {
        parent.classList.add('sidebar__item--expanded')
      }
    })
  })
})

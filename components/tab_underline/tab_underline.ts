/**
 * Composant : tab_underline
 * Gestion de la navigation entre onglets underline.
 * Reprend la même logique que tab_wrapper.js du design actuel,
 * adaptée au markup tab_underline.
 * Les panels sont scopés au parent du wrapper (pas document global).
 */
"use strict";

(function (): void {
  document.addEventListener("DOMContentLoaded", () => {
    document.addEventListener("click", (event: Event) => {
      const target = event.target as HTMLElement;
      const tabButton = target.closest<HTMLElement>(".tab-underline__item");
      if (!tabButton) return;

      const tabWrapper = tabButton.closest<HTMLElement>(".js-tabs");
      if (!tabWrapper) return;

      const tabId: string = tabButton.dataset.tabId ?? "";
      if (!tabId) return;

      // Scope : le conteneur parent du wrapper contient les panels associés
      const scope: HTMLElement = (tabWrapper.parentElement as HTMLElement) ?? document.body;

      // Mise à jour des boutons dans ce wrapper uniquement
      tabWrapper
        .querySelectorAll<HTMLElement>(".tab-underline__item")
        .forEach((button) => {
          button.classList.remove("tab-underline__item--active");
          button.setAttribute("aria-selected", "false");
        });

      tabButton.classList.add("tab-underline__item--active");
      tabButton.setAttribute("aria-selected", "true");

      // Mise à jour des panels dans le scope uniquement
      scope
        .querySelectorAll<HTMLElement>(".panel")
        .forEach((panel) => panel.classList.remove("panel--active"));

      const targetPanel = document.getElementById(`panel-${tabId}`);
      if (targetPanel) {
        targetPanel.classList.add("panel--active");
      }
    });
  });
})();

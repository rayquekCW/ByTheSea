import { createRouter, createWebHistory } from "vue-router";
import about from "../views/AboutView.vue";
import portConnections from "../views/PortConnections.vue";
import SkillsReportingView from "../views/SkillsReportingView.vue";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: about,
    },
    {
      path: "/portconnections",
      name: "port",
      component: portConnections,
    },
    {
      path: "/skillsreporting",
      name: "SkillsReportingView",
      component: SkillsReportingView,
    },
  ],
});

export default router;

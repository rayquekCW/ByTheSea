import { createRouter, createWebHistory } from 'vue-router'
import SkillsReportingView from '../views/SkillsReportingView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/skillsreporting',
      name: 'SkillsReportingView',
      component: SkillsReportingView
    },
  ]
})

export default router

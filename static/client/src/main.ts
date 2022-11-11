import { createApp, h } from 'vue'
import { createInertiaApp } from '@inertiajs/inertia-vue3'
import { InertiaProgress } from '@inertiajs/progress'
import './index.css'
// const modules = import.meta.glob('./dir/*.js')
// code produced by vite
// const modules = {
//   './dir/foo.js': () => import('./dir/foo.js'),
//   './dir/bar.js': () => import('./dir/bar.js')
// }
//

createInertiaApp({
  resolve: async (name) => {
    const pages = import.meta.glob('./Pages/**/*.vue')
    const page = ((await pages[`./Pages/${name}.vue`]()) as any).default

    return page
  },
  setup({ el, app, props, plugin }) {
    createApp({ render: () => h(app, props) })
      .use(plugin)
      .mount(el)
  },
})

InertiaProgress.init({
  color: '#29d',
})

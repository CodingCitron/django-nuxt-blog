export default {
  mode: 'univarsal',
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'blog',
    htmlAttrs: {
      lang: 'ko'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/css/main.css',
    '@/assets/css/global.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    // '~/plugins/axios'
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxt/postcss8',
    '@nuxtjs/composition-api/module',
    // ...
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next'
  ],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
    transpile: [
      'axios',
    ],
  },

  server: {
    port: 3000,
  },

  axios: {
    withCredentials: true,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
    },
    baseURL: 'http://127.0.0.1:8000/api/',
  },

  auth: {
    stategies: {
      local: {
        token: {
          prefix: 'access_token',
          property: 'access_token',
          maxAge: 900,
          type: 'Bearer'
        }
      },
      user: {
        property: 'user',
        autoFetch: true
      },
      endpoints: {
        signIn: { url: '/sign-in', method: 'post' },
        signUp: { url: '/sign-up', method: 'post' },
        user: { url: 'user', method: 'get' },
        refresh: { url: '/token/refresh', method: 'post' }
      }
    }
  }
}

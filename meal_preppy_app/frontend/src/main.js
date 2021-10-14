import { createApp } from 'vue';
import { createStore } from 'vuex';
import App from './App.vue';
import router from './router';

require('@/assets/main.scss');

const store = createStore({
  state() {
    return {
      authenticated: false,
    };
  },
  mutations: {
    setAuthentication(state, status) {
      state.authenticated = status;
    },
  },
});

router.beforeEach((to, from, next) => {
  if (
    to.name !== 'LoginForm'
    && to.name !== 'Index'
    && to.name !== 'SignUpForm'
    && !store.state.authenticated
  ) {
    next({ name: 'LoginForm' });
  } else {
    next();
  }
});

createApp(App)
  .use(router)
  .use(store)
  .mount('#app');

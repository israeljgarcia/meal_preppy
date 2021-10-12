import { createRouter, createWebHistory } from 'vue-router';

import SignUpForm from '../views/SignUpForm.vue';
import Recipies from '../views/Recipies.vue';
import Pantry from '../views/Pantry.vue';
import PantryIngredientForm from '../views/PantryIngredientForm.vue';
import LoginForm from '../views/LoginForm.vue';
import Home from '../views/Home.vue';
import Index from '../views/Index.vue';

const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index,
  },
  {
    path: '/signup',
    name: 'SignUpForm',
    component: SignUpForm,
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'LoginForm',
    component: LoginForm,
  },
  {
    path: '/recipes',
    name: 'Recipies',
    component: Recipies,
  },
  {
    path: '/pantry/ingredients',
    name: 'Pantry',
    component: Pantry,
  },
  {
    path: '/pantry/form',
    name: 'PantryIngredientForm',
    component: PantryIngredientForm,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

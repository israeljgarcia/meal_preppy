import axios from 'axios';

// axios setup
axios.defaults.headers.common.Authorization = `Bearer ${localStorage.getItem(
  'token',
)}`;

import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { login as enter, register } from '../../auth/auth.service';

export const fetchLogin = createAsyncThunk('user/fetchUser', async (login: any, password: any) => {
  const res = await enter(login, password);
  return res;
});

const LoginSlice = createSlice({
  name: 'user',
  initialState: {
    user: {},
    isLoading: false,
    hasError: false,
  },
  reducers: {
    logout: (state) => {
      state.user = {};
      state.isLoading = false;
      state.hasError = false;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchLogin.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchLogin.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchLogin.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
  },
});

export const selectUser = (state: { user: { user: any } }) => state.user.user;
export const selectLoading = (state: { user: { isLoading: any } }) => state.user.isLoading;
export const selectError = (state: { user: { hasError: any } }) => state.user.hasError;
export const { logout } = LoginSlice.actions;

export default LoginSlice.reducer;

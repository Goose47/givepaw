import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { login as enter, register } from '../../auth/auth.service';

// export const fetchLogin = createAsyncThunk('user/fetchLogin', async (login: any, password: any) => {
//   const res = await enter(login, password);
//   return res;
// });

export const fetchRegister = createAsyncThunk('user/fetchRegister', async (data: any) => {
  const res = await register(
    data.email,
    data.phone,
    data.password,
    data.name,
    data.surname,
    data.patronymic,
    data.city,
    data.image
  );
  return res;
});

const UserSlice = createSlice({
  name: 'user',
  initialState: {
    user: {},
    isLoading: false,
    hasError: false,
  },
  reducers: {
    // logout: (state) => {
    //   state.user = {};
    //   state.isLoading = false;
    //   state.hasError = false;
    // },
  },
  extraReducers: (builder) => {
    builder
    //   .addCase(fetchLogin.pending, (state, action) => {
    //     state.isLoading = true;
    //     state.hasError = false;
    //   })
    //   .addCase(fetchLogin.pending, (state, action) => {
    //     state.isLoading = true;
    //     state.hasError = false;
    //   })
    //   .addCase(fetchLogin.fulfilled, (state, action) => {
    //     state.user = action.payload;
    //     state.isLoading = false;
    //     state.hasError = false;
    //   })
      .addCase(fetchRegister.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchRegister.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      })
      // .addCase(fetchRegister.rejected, (state, action) => {
      //   state.hasError = true;
      //   state.isLoading = false;
      // });
  },
});

export const selectUser = (state: { user: { user: any } }) => state.user.user;
export const selectLoading = (state: { user: { isLoading: any } }) => state.user.isLoading;
export const selectError = (state: { user: { hasError: any } }) => state.user.hasError;
// export const { logout } = UserSlice.actions;

export default UserSlice.reducer;

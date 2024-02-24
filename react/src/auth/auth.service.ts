import axios from 'axios';

export const register = async (
  username: string,
  name: string,
  phone: string,
  surname: string,
  patronymic: string,
  email: string,
  password: string,
  city: number,
  image: Blob
) => {
  const formData = new FormData();
  formData.append('username', username);
  formData.append('name', name);
  formData.append('phone', phone);
  formData.append('surname', surname);
  formData.append('patronymic', patronymic);
  formData.append('email', email);
  formData.append('password', password);
  formData.append('city_id', city.toString());
  formData.append('avatar', image);
  try {
    const response = await axios.post('auth/register', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        withCredentials: true,
      },
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const login = async (username: string, password: string) => {
  try {
    const response = await axios.post('auth/login', { username, password });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

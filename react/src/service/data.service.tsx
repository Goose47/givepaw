import axios from 'axios';

export const getBreeds = async (pet_type_id: any) => {
  try {
    const response = await axios.get(`pets/breeds/${pet_type_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getUser = async () => {
  try {
    const response = await axios.get('users/user/info');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getBloodTypes = async (pet_type_id: any) => {
  try {
    const response = await axios.get(`blood_group/${pet_type_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
export const getVaccines = async () => {
  try {
    const response = await axios.get('pets/vaccinations');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const editSocial = async (telegram: string, vk: string) => {
  try {
    const response = await axios.put('https://dev.api.uvuv643.ru/user_networks/', {telegram, vk});
    console.log(editSocial);
    console.log(response.data);
    return response.data;
  } catch (error : any) {
    if (error.response.status === 400) {
      alert(error.response.data.detail)
    }
  }
};

export const getSocial = async () => {
  try {
    const response = await axios.get('user_networks');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getMostNecessary = async () => {
  try {
    const response = await axios.get('blood_bank/necessary');
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

export const editUser = async (surname: string, name: string, patronymic: string, username: string, email: string, city_id: string) => {
  try {
    const response = await axios.post('https://dev.api.uvuv643.ru/users/user', {surname, name, patronymic,username, email, city_id });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const editPassword = async (password: string) => {
  try {
    const response = await axios.put('users/user/change_password', {password});
    return response.data;
  } catch (error) {
    console.error(error);
  }
};


export const getAnimalTypes = async () => {
  try {
    const response = await axios.get('pets/pet_types');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getComponentTypes = async () => {
  try {
    const response = await axios.get('pets/blood_components');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getClinics = async () => {
  try {
    const response = await axios.get('clinics');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const createPet = async (
  animalType: string,
  breed: string,
  bloodGroup: string,
  petName: string,
  bloodComponent: string,
  image: string,
  age: string,
  weight: string,
  vaccinations: string[],
  user: any
) => {
  try {
    const response = await axios.post('pets', {
      blood_group_id: bloodGroup,
      breed_id: breed,
      pet_type_id: animalType,
      avatar_id: image,
      name: petName,
      age: age,
      weight: weight,
      user_id: user.id,
      vaccinations: vaccinations,
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const createdDonor = async (pet_id: number, city_id: number, clinic_id: number) => {
  try {
    const response = await axios.post('donors');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const createRecipient = async (
  reason: string,
  blood_component_id: number,
  blood_amount: number,
  donor_amount: number,
  pet_id: number,
  clinic_id: number,
  end_actual_date: string
) => {
  try {
    const response = await axios.post('recipients');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getPets = async () => {
  try {
    const response = await axios.get('pets/my');
    return response.data;
  } catch (error : any) {
    if (error.response.status === 401) {
      window.location.replace("/login")
    }
  }
};

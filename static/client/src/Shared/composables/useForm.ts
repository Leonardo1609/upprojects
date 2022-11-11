import { SchemaOf, ValidationError } from 'yup'
import { useForm as useInertiaForm } from '@inertiajs/inertia-vue3'

export const useForm = <T extends {}>(
  initialValues: T,
  schema?: SchemaOf<T>
) => {
  const form = useInertiaForm<T>({ ...initialValues })

  const handleSubmit = async (callBack: () => any) => {
    try {
      if (schema) {
        await schema.validate(form, {
          abortEarly: false,
        })
        form.clearErrors()
        callBack()
      }
      callBack()
    } catch (err) {
      if (err instanceof ValidationError) {
        form.clearErrors()
        err.inner.forEach((value) => {
          if (value.path) {
            form.setError(value.path as keyof T, value.message)
          }
        })
      }
    }
  }

  return {
    form,
    resetErrors: form.clearErrors(),
    handleSubmit,
  }
}

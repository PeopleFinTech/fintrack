import { useForm } from "react-hook-form"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"
import { Link, useNavigate } from "react-router-dom"
import { useDispatch } from "react-redux"
import { setToken } from "../../../redux/slices/auth"

const loginSchema = z
    .object({
        email: z.email("Enter a valid email").min(1, { message: "Email is required" }),
        password: z
            .string("Enter your password")
            .min(8, { message: "Password must be at least 8 characters" })
            .max(72, { message: "Password must be less than 72 characters" }),
    })


export default function LoginPage() {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const {
        register,
        handleSubmit,
        formState: { errors, isSubmitting },
    } = useForm({
        resolver: zodResolver(loginSchema),
        defaultValues: { email: "", password: "" },
    })

    const onSubmit = async (values) => {
        const { email, password } = values
        const formData = new FormData()
        formData.append("email", email)
        formData.append("password", password)

        const res = await fetch("http://localhost/api/v1/auth/login", {
            method: "POST",
            body: formData,
        })
        const data = await res.json().catch(() => null)

        if (!res.ok) {
            const message =
            data?.detail?.[0]?.msg ||
            data?.message ||
            "Invalid email or password"
          setError("root", { message })
          return
    }
    console.log("LOGIN SUCCESS:", data)
  
    navigate("/dashboard")
  }

    return (
        <div className="min-h-screen bg-gray-50 text-gray-900">
            <div className="mx-auto max-w-7xl px-6 py-10">
                {/* Top bar */}
                <div className="flex items-center justify-between">
                    <div className="font-bold text-xl">FinTrack</div>
                    <Link
                        to={'/'}
                        className="text-sm font-medium text-gray-600 hover:text-blue-600"
                    >
                        Back to home
                    </Link>
                </div>

                <div className="mt-10 grid gap-10 lg:grid-cols-2 items-center">
                    {/* Left */}
                    <div className="hidden lg:block">
                        <h1 className="text-4xl font-bold leading-tight">Welcome back 👋</h1>
                        <p className="mt-4 text-gray-600 max-w-md">
                            Sign in to continue to your dashboard and manage your account.
                        </p>

                        <div className="mt-8 grid gap-4 max-w-md">
                            <div className="rounded-2xl border bg-white p-5">
                                <div className="font-semibold">Secure access</div>
                                <div className="text-sm text-gray-600 mt-1">
                                    Your data stays protected with modern security practices.
                                </div>
                            </div>
                            <div className="rounded-2xl border bg-white p-5">
                                <div className="font-semibold">Fast workflow</div>
                                <div className="text-sm text-gray-600 mt-1">
                                    Pick up where you left off in seconds.
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Right */}
                    <div className="mx-auto w-full max-w-md">
                        <div className="rounded-2xl border bg-white p-6 shadow-sm">
                            <h2 className="text-2xl font-bold">Login</h2>
                            <p className="mt-2 text-sm text-gray-600">
                                Enter your email and password to sign in.
                            </p>

                            {/* Google */}
                            <button
                                type="button"
                                onClick={() => alert("Hook this to your Google OAuth flow")}
                                className="mt-6 w-full rounded-xl border bg-white px-4 py-3 text-sm font-semibold hover:bg-gray-50 flex items-center justify-center gap-3"
                            >
                                <span className="inline-flex h-5 w-5 items-center justify-center rounded-full border">
                                    G
                                </span>
                                Continue with Google
                            </button>

                            <div className="my-6 flex items-center gap-3">
                                <div className="h-px flex-1 bg-gray-200" />
                                <span className="text-xs text-gray-500">OR</span>
                                <div className="h-px flex-1 bg-gray-200" />
                            </div>

                            <form 
                            onSubmit={handleSubmit(onSubmit)}
                                className="grid gap-4">
                                <div>
                                    <label className="text-sm font-medium">Email</label>
                                    <input
                                        type="email"
                                        placeholder="you@example.com"
                                        className={["mt-1 w-full rounded-xl border px-4 py-3 text-sm outline-none focus:ring-2 focus:ring-blue-200",
                                            errors.email ? "border-red-400 focus:ring-red-200" : "focus:ring-blue-200",
                                        ].join(" ")} 
                                        {...register("email")} 
                                    />
                                </div>
                                {errors.email && (
                                    <p className="mt-1 text-xs text-red-600">{errors.email.message}</p>
                                )}

                                <div>
                                    <label className="text-sm font-medium">Password</label>
                                    <input
                                        type="password"
                                        placeholder="••••••••"
                                        className={[
                                            "mt-1 w-full rounded-xl border px-4 py-3 text-sm outline-none focus:ring-2",
                                            errors.password ? "border-red-400 focus:ring-red-200" : "focus:ring-blue-200",
                                        ].join(" ")}
                                        {...register("password")}
                                    />
                                    {errors.password && (
                                        <p className="mt-1 text-xs text-red-600">{errors.password.message}</p>
                                    )}
                                </div>

                                <div className="flex items-center justify-between">
                                    <label className="flex items-center gap-2 text-sm text-gray-600">
                                        <input type="checkbox" className="h-4 w-4 rounded border" />
                                        Remember me
                                    </label>
                                    <a
                                        href="#"
                                        className="text-sm font-medium text-blue-600 hover:text-blue-700"
                                    >
                                        Forgot password?
                                    </a>
                                </div>

                                <button
                                    disabled={isSubmitting}
                                    type="submit"
                                    className="mt-2 w-full rounded-xl bg-blue-600 px-4 py-3 text-sm font-semibold text-white hover:bg-blue-700 disabled:opacity-60"
                                >
                                    {isSubmitting ? "Signing in..." : "Sign in"}
                                </button>
                            </form>

                            <p className="mt-6 text-center text-sm text-gray-600">
                                Don’t have an account?{" "}
                                <a href="/register" className="font-semibold text-blue-600 hover:text-blue-700">
                                    Sign up
                                </a>
                            </p>
                        </div>

                        <p className="mt-4 text-center text-xs text-gray-500">
                            By continuing, you agree to our{" "}
                            <a href="#" className="underline hover:text-gray-700">Terms</a> and{" "}
                            <a href="#" className="underline hover:text-gray-700">Privacy Policy</a>.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    )
}

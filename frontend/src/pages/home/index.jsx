import { useNavigate } from "react-router-dom"

export default function Home() {
  const navigate = useNavigate()
  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      {/* Navbar */}
      <header className="border-b bg-white">
        <div className="mx-auto max-w-7xl px-6 py-4 flex items-center justify-between">
          <h1 className="text-xl font-bold">FinTrack</h1>

          <nav className="hidden md:flex gap-6 text-sm font-medium">
            <a href="#" className="hover:text-blue-600">Home</a>
            <a href="#" className="hover:text-blue-600">Features</a>
            <a href="#" className="hover:text-blue-600">Pricing</a>
            <a href="#" className="hover:text-blue-600">How it works</a>
          </nav>

          <div className="flex gap-4">
            <button
              onClick={() => navigate("/register")}
              className="rounded-lg bg-blue-600 px-4 py-2 text-sm text-white hover:bg-blue-700"
            >
              Register
            </button>

            <button
              onClick={() => navigate("/login")}
              className="rounded-lg border px-6 py-2 text-sm hover:bg-gray-100"
            >
              Login
            </button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="mx-auto max-w-7xl px-6 py-24 grid gap-12 md:grid-cols-2 items-center">
        <div>
          <h2 className="text-4xl font-bold leading-tight mb-6">
            Know where your money goes, every month
          </h2>
          <p className="text-gray-600 mb-8">
            Log daily spending, organize by category, and see exactly where your money goes all in one place.
          </p>

          <div className="flex gap-4">
            <button className="rounded-lg bg-blue-600 px-6 py-3 text-white hover:bg-blue-700">
              Start Free
            </button>
            <button className="rounded-lg border px-6 py-3 hover:bg-gray-100">
              Learn More
            </button>
          </div>
        </div>

        {/* Hero Image Placeholder */}
        <div className="h-80 rounded-2xl bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center">
          <span className="text-gray-500">Hero Image</span>
        </div>
      </section>

      {/* Features */}
      <section className="bg-white py-20">
        <div className="mx-auto max-w-7xl px-6">
          <h3 className="text-2xl font-bold text-center mb-12">
            Why choose our platform?
          </h3>

          <div className="grid gap-8 md:grid-cols-3">
            {[
              { title: "Fast", desc: "Optimized performance with modern technologies." },
              { title: "Secure", desc: "Built with security best practices in mind." },
              { title: "Scalable", desc: "Grows with your business effortlessly." },
            ].map((feature, i) => (
              <div
                key={i}
                className="rounded-xl border p-6 hover:shadow-md transition"
              >
                <h4 className="font-semibold text-lg mb-2">{feature.title}</h4>
                <p className="text-gray-600 text-sm">{feature.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="bg-blue-600 py-20">
        <div className="mx-auto max-w-7xl px-6 text-center text-white">
          <h3 className="text-3xl font-bold mb-4">
            Ready to get started?
          </h3>
          <p className="mb-8 text-blue-100">
            Join thousands of users building better products today.
          </p>
          <button className="rounded-lg bg-white px-6 py-3 text-blue-600 font-medium hover:bg-gray-100">
            Create an Account
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t bg-white">
        <div className="mx-auto max-w-7xl px-6 py-6 text-sm text-gray-500 flex justify-between">
          <span>© 2025 MyApp</span>
          <div className="flex gap-4">
            <a href="#" className="hover:text-blue-600">Privacy</a>
            <a href="#" className="hover:text-blue-600">Terms</a>
          </div>
        </div>
      </footer>
    </div>
  )
}

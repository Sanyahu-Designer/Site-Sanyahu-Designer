/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
  ],
  darkMode: 'class',
  theme: {
    screens: {
      'xs': '375px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        md: '3rem',
        lg: '4rem',
        xl: '5rem',
        '2xl': '6rem',
      },
    },
    extend: {
      colors: {
        primary: 'rgb(var(--primary) / <alpha-value>)',
        'primary-dark': 'rgb(var(--primary-dark) / <alpha-value>)',
        secondary: 'rgb(var(--secondary) / <alpha-value>)',
        accent: 'rgb(var(--accent) / <alpha-value>)',
        background: 'rgb(var(--background) / <alpha-value>)',
        text: 'rgb(var(--text) / <alpha-value>)',
        'text-light': 'rgb(var(--text-light) / <alpha-value>)',
        success: '#00B884',
        warning: '#FFB82E',
        error: '#FF4757',
        'gold-primary': 'rgb(var(--gold-primary) / <alpha-value>)',
        'gold-light': 'rgb(var(--gold-light) / <alpha-value>)',
        'gold-dark': 'rgb(var(--gold-dark) / <alpha-value>)',
        'deep-navy': 'rgb(var(--deep-navy) / <alpha-value>)',
        'slate-blue': 'rgb(var(--slate-blue) / <alpha-value>)',
        'cool-gray': 'rgb(var(--cool-gray) / <alpha-value>)',
        'pearl-white': 'rgb(var(--pearl-white) / <alpha-value>)',
      },
      fontFamily: {
        sans: ['Roboto', 'Inter', 'Space Grotesk', 'sans-serif'],
        display: ['Space Grotesk', 'Roboto', 'sans-serif'],
        body: ['Inter', 'Roboto', 'sans-serif'],
      },
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.5rem' }],
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
        '5xl': ['3rem', { lineHeight: '1.16' }],
        '6xl': ['3.75rem', { lineHeight: '1.15' }],
      },
      animation: {
        'fade-in-up': 'fadeInUp 0.5s ease-out forwards',
        'spin-slow': 'spin 20s linear infinite',
        'fade-up': 'fadeInUp 1s ease-out forwards',
        'fade-in': 'fadeIn 0.5s ease-out forwards',
        'scale-in': 'scaleIn 0.4s ease-out forwards',
        'bounce-slow': 'bounce 3s linear infinite',
        'typing': 'typing 3.5s steps(40, end)',
        'blink': 'blink .75s step-end infinite',
        'float': 'float 6s ease-in-out infinite',
      },
      keyframes: {
        fadeInUp: {
          '0%': {
            opacity: '0',
            transform: 'translateY(20px)',
          },
          '100%': {
            opacity: '1',
            transform: 'translateY(0)',
          },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        fadeUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        scaleIn: {
          '0%': { opacity: '0', transform: 'scale(0.9)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
        typing: {
          'from': { width: '0' },
          'to': { width: '100%' }
        },
        blink: {
          'from, to': { 'border-color': 'transparent' },
          '50%': { 'border-color': 'white' }
        },
        float: {
          '0%, 100%': {
            transform: 'translateY(0)',
          },
          '50%': {
            transform: 'translateY(-20px)',
          },
        },
      },
      spacing: {
        '128': '32rem',
      },
      borderRadius: {
        'xl': '1rem',
        '2xl': '2rem',
      },
      boxShadow: {
        'soft': '0 2px 15px rgb(0 0 0 / 0.05)',
        'card': '0 10px 30px rgb(0 0 0 / 0.1)',
        'card-hover': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
      },
      backdropBlur: {
        xs: '2px',
      },
      backgroundImage: {
        'grid-pattern': "url(\"data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23000000' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E\")",
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}

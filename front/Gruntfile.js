'use strict';

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    // Metadata.
    pkg: grunt.file.readJSON('package.json'),
    banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - ' +
      '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
      '<%= pkg.homepage ? "* " + pkg.homepage + "\\n" : "" %>' +
      '* Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>;' +
      ' Licensed <%= _.pluck(pkg.licenses, "type").join(", ") %> */\n',
    // Task configuration.
    jshint: {
      options: {
        jshintrc: '.jshintrc'
      },
      gruntfile: {
        src: 'Gruntfile.js'
      },
      vendors: {
        options: {
          jshintrc: './src/assets/js/.jshintrc'
        },
        src: './src/assets/js/vendors/**/*.js'
      },
      components: {
        options: {
          jshintrc: './src/assets/js/.jshintrc'
        },
        src: ['./src/assets/js/components/**/*.js', '!./src/assets/js/components/jquery.hammer.js']
      }
    },
    concat: {
      options: {
        banner: '<%= banner %>',
        stripBanners: true
      },
      build: {
        src: ['./src/assets/js/vendors/**/*.js', './src/assets/js/components/**/*.js'],
        dest: './src/assets/js/script.js'
      }
    },
    uglify: {
      options: {
        banner: '<%= banner %>'
      },
      build: {
        src: '<%= concat.build.dest %>',
        dest: './src/assets/js/script.min.js'
      },
    },
    compass: {
      // TODO: Should I use these settings or config.rb
      dev: {
        options: {
          require : ['compass', 'breakpoint', 'rgbapng'],
          basePath: 'src/assets',
          sassDir : 'sass',
          cssDir: 'css',
          imagesDir: 'img',
          fontsDir: 'fonts',
          javascriptsPath: 'js',
          outputStyle: 'expanded',
          noLineComments: false,
          debugInfo: true
        }
      },
      styleguide: {
        // Temporary, This will get moved and deleted from src
        options: {
          require : ['compass', 'breakpoint', 'rgbapng'],
          basePath: 'src/assets',
          sassDir : 'sass',
          cssDir: 'css-sg',
          imagesDir: 'img',
          fontsDir: 'fonts',
          javascriptsPath: 'js',
          outputStyle: 'expanded',
          noLineComments: true
        }
      },
      prod: {
        options: {
          require : ['compass', 'breakpoint', 'rgbapng'],
          basePath: 'src/assets',
          sassDir : 'sass',
          cssDir: 'css',
          imagesDir: 'img',
          fontsDir: 'fonts',
          javascriptsPath: 'js',
          outputStyle: 'compressed',
          noLineComments: true,
          environment: 'production',
          debugInfo: false
        }
      },
      clean: {
        options: {
          clean: true,
          basePath: 'src/assets',
          sassDir : 'sass',
          cssDir: 'css',
          imagesDir: 'img',
          fontsDir: 'fonts',
          javascriptsPath: 'js',
          outputStyle: 'compressed',
          noLineComments: true,
          environment: 'production',
          debugInfo: false
        }
      }
    },
    copy: {
      css: {
        files: [
          {
            expand: true,
            cwd: 'src/assets/css/',
            src: ['**'],
            dest: '_site/assets/css/'
          }
        ]
      },
      cssSg: {
        files: [
          {
            expand: true,
            cwd: 'src/assets/css-sg/',
            src: ['**'],
            dest: '_site/assets/css-sg/'
          }
        ]
      },
      js: {
        files: [
          {
            expand: true,
            cwd: 'src/assets/js/',
            src: ['**'],
            dest: '_site/assets/js/'
          }
        ]
      },
      images: {
        files: [
          {
            expand: true,
            cwd: 'src/assets/img/',
            src: ['**'],
            dest: '_site/assets/img/'
          }
        ]
      },
      fonts: {
        files: [
          {
            expand: true,
            cwd: 'src/assets/fonts/',
            src: ['**'],
            dest: '_site/assets/fonts/'
          }
        ]
      },
      styleguide: {
        files: [
          {
            expand: true,
            cwd: 'src/styleguide/',
            src: ['**'],
            dest: '_site/styleguide/'
          }
        ]
      }
    },
    shell: {
      jsdelete: {
        command: 'rm -rf _site/assets/js/*',
        stdout: false
      },
    },
    connect: {
      livereload: {
        options: {
          port: 4000,
          base: '_site'
        }
      }
    },
    open : {
      server : {
        path: 'http://localhost:4000'
      }
    },
    watch: {
      options: {
        livereload: true,
      },
      gruntfile: {
        files: '<%= jshint.gruntfile.src %>',
        tasks: ['jshint:gruntfile']
      },
      sass: {
        files: 'src/assets/sass/**/*.scss',
        tasks: ['compass:dev', 'compass:styleguide', 'copy:css', 'copy:cssSg']
      },
      js: {
        files: ['<%= jshint.vendors.src %>', '<%= jshint.components.src %>'],
        tasks: ['jshint:components', 'concat', 'shell:jsdelete', 'copy:js']
      },
      images: {
        files: 'src/img/**/*',
        tasks: ['copy:images']
      },
      fonts: {
        files: 'src/fonts/**/*',
        tasks: ['copy:fonts']
      },
      styleguide: {
        files: 'src/styleguide/**/*',
        tasks: ['copy:styleguide']
      },
    },
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-shell');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-open');

  // Default task.
  grunt.registerTask('default', ['jshint:components', 'concat', 'uglify', 'compass:clean', 'compass:styleguide', 'compass:prod', 'copy:cssSg', 'copy:css']);

  // Watch and open server in browser
  grunt.registerTask('wo', ['connect', 'open:server', 'watch']);

  // Watch
  grunt.registerTask('w', ['connect', 'watch']);

};
